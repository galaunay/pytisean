# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN surrogates testing tools wrappers
"""

from ..tiseanwrapper import tisean


__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def surrogates(data, nmb_surr=1, nmb_it=None, spec=False,
               random_seed=1, nmb_data_to_use=None, ignored_row=0,
               nmb_col_to_read=1, col_to_read=1, output_file=None, verbose=0):
    """
    Creates surrogate data with the same Fourier amplitudes and the
    same distribution of values.

    It is advisable to select a suitable sub-sequence to minimize
    end effects by using 'before' preparing surrogates.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    nmb_surr: integer
        Number of surrogates (default to 1)
    nmb_it integer, optional
        Number of iterations (by default, continue until no further changes)
    spec: bool, optional
        Make spectrum exact rather than distribution (default to distributions)
    random_seed: integer
        Seed for random numbers (default to 1)
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
    nmb_col_to_read: integer
        Number of columns to be read (default to 1)
    col_to_read : integer
        Number of columns to be read if 'time_serie' is a file path
        (Default to 1).
    output_file : string
        Output field path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    surr : nxnm_surr array
        Resulting surrogates data
    """
    # prepare arguments
    args = "-n{} -I{} -x{} -m{} -c{} -V{}"\
           .format(nmb_surr, random_seed, ignored_row,
                   nmb_col_to_read, col_to_read, verbose)
    if nmb_it is not None:
        args += " -i{}".format(nmb_it)
    if spec:
        args += " -S"
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('surrogates', args, input_data=data,
                      output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res


def endtoend(data, nmb_data_to_use=None, ignored_row=0,
             nmb_col_to_read=1, col_to_read=1, output_file=None, verbose=0):
    """
    Determine the effect of an end-to-end mismatch on the
    autocorrelation structure for various sub-sequence lenths.

    It is important to avoid jumps and phase slips that occur when the
    data is periodically continued when making Fourier based surrogates,
    e.g. with surrogates.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
    nmb_col_to_read: integer
        Number of columns to be read (default to 1)
    col_to_read : integer
        Number of columns to be read if 'time_serie' is a file path
        (Default to 1).
    output_file : string
        Output field path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    surr : nxnm_surr array
        Resulting surrogates data

    """
    # prepare arguments
    args = "-x{} -m{} -c{} -V{}"\
           .format(ignored_row,
                   nmb_col_to_read, col_to_read, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('endtoend', args, input_data=data,
                      output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res


def predict(data, delay, dim, radius=None, rel_radius=None,
            forecast=1, nmb_data_to_use=None, ignored_row=0,
            col_to_read=1, output_file=None, verbose=0):
    """
    Performs locally constant predictions on scalar time series and
    prints the root mean squared prediction error.

    Parameters
    ----------
    delay: integer
        Delay
    dim: integer
        Embedding dimension
    radius: number, optional
        Absolute radius of neighbourhoods
    rel_radius: number, optional
        Radius of the neighbourhoods relative to the standard deviation
    forecast: integer
         Time steps ahead forecast (default to one step)
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
    col_to_read : integer
        Number of columns to be read if 'time_serie' is a file path
        (Default to 1).
    output_file : string
        Output field path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    """
    # prepare arguments
    args = "-d{} -m{} -s{} -x{} -c{} -V{}"\
           .format(delay, dim, forecast, ignored_row, col_to_read,
                   verbose)
    if radius is not None:
        args += " -r{}".format(radius)
    elif rel_radius is not None:
        args += " -v{}".format(rel_radius)
    else:
        raise ValueError("You should specify at least 'radius' or "
                         "'rel_radius'")
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('predict', args, input_data=data,
                      output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res
