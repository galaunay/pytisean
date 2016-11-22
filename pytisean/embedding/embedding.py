# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN embedding tools wrappers
"""

from ..tiseanwrapper import tisean


def delay(data, dimension=2, vector_format=None, vector_delay=1, delays=None,
          nmb_data_to_use=None, ignored_row=0, ignored_col=1, col_to_read=1,
          output_file=None, verbose=0):
    """
    Produces delay vectors either from a scalar or
    from a multivariate time series.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    dimension : number
        Embedding dimension (default to 2).
    vector_format : array
        Format of the embedding vector (see tisean help for more details)
        (default to None).
    vector_delay : number
        Delay of the embedding vector (default to 1).
    delays : array
        List of individuals delays (default to None).
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
    ignored_col : integer
        Number of file columns to ignore if 'time_serie' is a file path
        (Default to 1).
    col_to_read : integer
        Number of columns to be read if 'time_serie' is a file path
        (Default to 1).
    output_file : string
        Output fiel path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    xy : list of [x, y] tuples
        Successive iterations of the Henon map.
    """
    # prepare arguments
    args = "-m{} -d{} -x{} -M{} -c{} -V{}" \
           .format(dimension, vector_delay, ignored_row, ignored_col,
                   col_to_read, verbose)
    if vector_format is not None:
        args += " -F{}".format(vector_format)
    if delays is not None:
        args += " -D{}".format(delays)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('delay', args, input_data=data, output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res


def mutual(data, maximum_delay=20, box_nmb=16, nmb_data_to_use=None,
           ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Estimates the time delayed mutual information of the data.

    It is the simplest possible realization. It uses a fixed mesh of boxes.
    No finite sample corrections are implemented so far.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    maximum_delay : integer
        Maximal time delay (default to 20).
    box_nmb : integer
        Number of boxes for the partition.
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
    col_to_read : integer
        Number of columns to be read if 'time_serie' is a file path
        (Default to 1).
    output_file : string
        Output file path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    occupied_boxes : integer
        Number of occupied boxes
    shannon_entropy : number
        Shannon number, normalized by the number of occupied boxes.
    mutual_info : list of [tau, mu] tuples
        delays and associated mutual information.
    """
    # prepare arguments
    args = "-b{} -D{} -x{} -c{} -V{}" \
           .format(box_nmb, maximum_delay, ignored_row, col_to_read, verbose)
    if nmb_data_to_use is not None:
        args += "-l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('delay', args, input_data=data, output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res

def poincare():
    pass

def extrema():
    pass

def upo():
    pass

def upoembed():
    pass

def false_nearest():
    pass
