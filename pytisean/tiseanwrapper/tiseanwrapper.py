# -*- coding: utf-8 -*-
#!/usr/env python3

""" Wrapper to TISEAN binaries. """

import tempfile
import subprocess
import os
import numpy as np


# For temporary files
TMPDIR = r'/tmp/pytisean/'
TMPPREFIX = 'pytisean_temp_'
if not os.path.isdir(TMPDIR):
    os.makedirs(TMPDIR)

def gentmpfile():
    """Generate temporary file and return file handle."""
    if not os.path.isdir(TMPDIR):
        os.mkdir(TMPDIR)
    fhandle = tempfile.mkstemp(prefix=TMPPREFIX,
                               dir=TMPDIR,
                               text=True)
    return fhandle[1]


def is_exec(command):
    """Test if a command is executable."""
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
    fpath, _ = os.path.split(command)
    if fpath:
        if is_exe(command):
            return True
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, command)
            if is_exe(exe_file):
                return True
    return False


def tisean(command, args, input_data=None, output_file=None):
    """
    Run a TISEAN command.

    Parameters
    ----------
    command : string
        Tisean routine
    args : list of string
        Arguments for the tisean routine.
        One argument per string (ex: ['-V1', '-d2', '-x100']).
    input_data : array or file path
        Input data for the tisean command (if necessary).
        (Can be a file path or an array of values).
    output_file : file path, optional
        Output file path.
        If 'None' (default), return the results.
    """
    # Return values if something fails
    res = None
    err_string = 'Something failed!'
    # Handles files (create temporary files if necessary)
    if input_data is not None:
        is_input_data = True
        if isinstance(input_data, str):
            fullname_in = input_data
            is_input_file = True
        else:
            fullname_in = gentmpfile()
            is_input_file = False
            np.savetxt(fullname_in, input_data, delimiter='\t')
    else:
        is_input_data = False
        is_input_file = False
    if output_file is not None:
        fullname_out = output_file
        is_output_file = True
    else:
        fullname_out = gentmpfile()
        is_output_file = False
    # check if command exist
    if not is_exec(command):
        raise Exception("'{}' command not on path".format(command))
    # add paths to args
    args += ["-o", "{}".format(fullname_out)]
    if is_input_data:
        args += [fullname_in]
    # Need cleanup temporary files even if the command fails
    try:
        # Call the wanted command
        subp = subprocess.Popen([command] + args,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        # Communicate with the subprocess
        (_, err_bytes) = subp.communicate()
        try:
            subp.kill()
        except OSError:
            pass
        # Check if tisean error occured
        err_string = err_bytes.decode('utf-8')
        if len(err_string) != 0:
            raise Exception("\n=== TISEAN ERROR ===\n"
                            + "=== Launched command:\n    {}\n"
                            .format(" ".join([command] + args))
                            + "=== Tisean said: \n    " + err_string)
        # Read the temporary 'out' file
        if not is_output_file:
            res = np.loadtxt(fullname_out)
    # Cleanup
    finally:
        if not is_input_file and is_input_data:
            os.remove(fullname_in)
        if not is_output_file:
            os.remove(fullname_out)
    # Return
    return res, err_string
