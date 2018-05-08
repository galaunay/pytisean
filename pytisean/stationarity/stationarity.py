# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN stationarity tools wrappers
"""

import warnings

from ..tiseanwrapper import tisean


def recurr(data, compo_nmb=1, dim=2, delay=1, neigh_size=None,
           perc_pts=100.0, nmb_data_to_use=None, ignored_row=1,
           col_to_read=1, output_file=None, verbose=0):
    """
    Produce a recurrence plot of the, possibly multivariate, data set.
    That means, for each point in the data set it looks for all points,
    such that the distance between these two points is smaller than a given
    size in a given embedding space.
    Be careful! Choosing a large value of 'neigh_size' can lead to really big
    files.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    compo_nmb : integer
        Number of component
    dimension : number
        Embedding dimension (default to 2).
    delay : array
        List of individuals delays (default to None).
    neigh_size : number
        Size of the neighborhood (Default to 'data_interval/1000').
    perc_pts : number
        Percentage of points actually saved (Default to 100.0)
        (Useful to reduce output size)
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
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
    xys : array
        Pairs of integers representing the indexes of the pairs of points
        having a distance smaller than 'neigh_size'.
    """
    # prepare arguments
    args = "-x{} -c{} -m{},{} -d{} -%{} -V{}"\
           .format(ignored_row, col_to_read,
                   compo_nmb, dim, delay, perc_pts, verbose)
    if neigh_size is not None:
        args += " -r{}".format(neigh_size)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('recurr', args, input_data=data, output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res

def stp(data, delay=1, dim=2, time_resolution=1, time_steps=100,
        levels_frac=0.05, nmb_data_to_use=None, ignored_row=1, col_to_read=1,
        output_file=None, verbose=0):
    """
    Computes a space time separation plot as discussed by Provenzale et al.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    delay : integer
        Time delay (default to 1).
    dimension : integer
        Embedding dimension (default to 2).
    time_resolution : integer
        Plot time resolution (default to 1).
    time_steps : integer
        Plot time steps (default to 100, at most 500).
    levels_frac : number
        Fraction at which to create levels (Default to 0.05, at least 0.01).
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
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
    ?
    """
    warnings.warn("The command 'stp' seems to have some trouble parsing "
                    "path with complex characters")
    # Check
    if data is None:
        raise Exception("'data' should not be none")
    # prepare arguments
    args = "-d{} -m{} -#{} -t{} -%{} -x{} -c{} -V{}"\
           .format(delay, dim, time_resolution, time_steps, levels_frac,
                   ignored_row, col_to_read, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('stp', args, input_data=data, output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res
