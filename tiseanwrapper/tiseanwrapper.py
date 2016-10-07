""" Wrapper to TISEAN binaries.
"""

import tempfile
import subprocess
import shlex
import os
from time import strftime
import numpy as np

__author__ = "Troels Bogeholm Mikkelsen"
__copyright__ = "Troels Bogeholm Mikkelsen 2016"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "bogeholm@nbi.ku.dk"
__status__ = "Development"

# Directory for temporary files
DIRSTR = r'/tmp/pytisean/'
# Prefix to identify these files
PREFIXSTR = 'pytisean_temp_'
# suffix - TISEAN likes .dat
SUFFIXSTR = '.dat'
ENV = {"PATH": "/home/glaunay/.local/bin"}

# We will use the present time as a part of the temporary file name
def genfilename():
    """ Generate a file name.
    """
    return PREFIXSTR + strftime('%Y-%m-%d-%H-%M-%S') + '_'

def gentmpfile():
    """ Generate temporary file and return file handle.
    """
    fhandle = tempfile.mkstemp(prefix=genfilename(),
                               suffix=SUFFIXSTR,
                               dir=DIRSTR,
                               text=True)
    return fhandle

def tisean(command, args, input_data=None, output_file=None):
    """
    Run a tisean command.

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
    output_data : file path, optional
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
            tf_in = gentmpfile()
            fullname_in = tf_in[1]
            is_input_file = False
            np.savetxt(fullname_in, input_data, delimiter='\t')
    else:
        is_input_data = False
        is_input_file = False
    if output_file is not None:
        fullname_out = output_file
        is_output_file = True
    else:
        tf_out = gentmpfile()
        fullname_out = tf_out[1]
        is_output_file = False
    # add paths to args
    args += ["-o {}".format(fullname_out)]
    if is_input_data:
        args += [fullname_in]
    # Need cleanup temporary files even if the command fails
    try:
        # Here we call TISEAN (or something else?)
        print(args)
        print(command)
        print(ENV)
        subp = subprocess.Popen(args,
                                executable=command,
                                env=ENV,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        # Communicate with the subprocess
        (_, err_bytes) = subp.communicate()
        err_string = err_bytes.decode('utf-8')
        # Read the temporary 'out' file
        if not is_output_file:
            res = np.loadtxt(fullname_out)
    # Cleanup
    finally:
        if not is_input_file and is_input_data:
            os.remove(fullname_in)
        if not is_output_file:
            os.remove(fullname_out)
        print(err_string)
    # We assume that the user wants the (error) message as well.
    return res, err_string


# def tiseano(command, *args):
#     """ TISEAN output wrapper.

#         Run 'command' and return result.

#         This function is meant as a wrapper around the TISEAN package.
#     """
#     # Return values if 'command' (or something else) fails
#     res = None
#     err_string = 'Something failed!'

#     # Check for user specified args
#     if '-o' in args:
#         raise ValueError('User is not allowed to specify an output file.')

#     # Handle to temporary file
#     tf_out = gentmpfile()
#     # Full names
#     fullname_out = tf_out[1]

#     # If no further args are specified, run this
#     if not args:
#         commandargs = [command, '-o', fullname_out]
#     # Otherwise, we concatenate the args and command
#     else:
#         # User can specify float args - we convert
#         arglist = [str(a) for a in args]
#         commandargs = [command] + arglist + ['-o', fullname_out]

#     # We will clean up irregardless of following success.
#     try:
#         # Here we call TISEAN (or something else?)
#         subp = subprocess.Popen(commandargs,
#                                 stdout=subprocess.PIPE,
#                                 stderr=subprocess.PIPE,
#                                 shell=False,
#                                 env={"PATH": "/home/glaunay/.local/bin"})

#         # Communicate with the subprocess
#         (_, err_bytes) = subp.communicate()
#         # Read the temporary 'out' file
#         res = np.loadtxt(fullname_out)
#         # We will read this
#         err_string = err_bytes.decode('utf-8')

#     # Cleanup
#     finally:
#         os.remove(fullname_out)

#     print(err_string)

#     # We assume that the user wants the (error) message as well.
#     return res, err_string
