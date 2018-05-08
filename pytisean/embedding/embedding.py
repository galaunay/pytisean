# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN embedding tools wrappers
"""

from ..tiseanwrapper import tisean

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


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
    if msg != "":
        print(msg)
    return res


def mutual(data, max_delay=20, box_nmb=16, nmb_data_to_use=None,
           ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Estimates the time delayed mutual information of the data.

    It is the simplest possible realization. It uses a fixed mesh of boxes.
    No finite sample corrections are implemented so far.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    max_delay : integer
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
           .format(box_nmb, max_delay, ignored_row, col_to_read, verbose)
    if nmb_data_to_use is not None:
        args += "-l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('mutual', args, input_data=data, output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res


def poincare(data, dim=2, delay=1, cross_comp=None, cross_dir=0,
             cross_pos=None, nmb_data_to_use=None, ignored_row=0,
             col_to_read=1, output_file=None, verbose=0):
    """
    Make a Poincaré section for time continuous scalar data sets along one of
    the coordinates of the embedding vector.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    dim : integer
        Embedding dimension (default 2).
    delay :
        Embedding delay (default 1).
    cross_comp : integer
        Component for the crossing (default to last).
    cross_dir : Direction of the crossing
        (0: from below, 1: from above).
    cross_pos : Position for the crossing
        (default to the data average).
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

    """
    # prepare arguments
    args = "-x{} -c{} -m{} -d{} -C{} -V{}" \
           .format(ignored_row, col_to_read, dim, delay, cross_dir,
                   verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if cross_comp is not None:
        args += " -q{}".format(cross_comp)
    if cross_pos is not None:
        args += " -a{}".format(cross_pos)
    args = args.split(" ")
    # run command
    res, msg = tisean('poincare', args, input_data=data,
                      output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res


def extrema(data, nmb_comp=2, comp=1, extrema="maxima",
            delta_t_min=0., nmb_data_to_use=None, ignored_row=0,
            col_to_read=None, output_file=None, verbose=0):
    """
    Determines the maxima (minima) of one component of a possibly multivariate
    time series. This corresponds to a Poincaré section at the zeros of the
    derivative. To get a better estimate of the extremum, a quadratic
    interpolation is done.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    nmb_comp : integer
        Number of components (default to 1).
    comp : integer
        Which component to maximine (or minimize).
        (default 1)
    extrema : string in {"minima", "maxima"}
        Determine if minima or maxima should be computed.
        (default to "maxima")
    delta_t_min : positive float
        Minimal time required between two extrema.
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
    col_to_read : integer
        Number of columns to be read if 'time_serie' is a file path
        (Default 1..nmb_comp).
    output_file : string
        Output file path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    """
    # prepare arguments
    args = "-x{} -m{} -w{} -t{} -V{}" \
           .format(ignored_row, nmb_comp, comp, delta_t_min, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if col_to_read is not None:
        args += " -c{}".format(col_to_read)
    if extrema == "minima":
        args += " -z"
    args = args.split(" ")
    # run command
    res, msg = tisean('extrema', args, input_data=data,
                      output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res


def upo():
    raise Exception("Not implemented yet")


def upoembed():
    raise Exception("Not implemented yet")


def false_nearest(data, min_dim=1, max_dim=5, comp_nmb=1, delay=1, ratio=2.0,
                  theiler_wind=0, nmb_data_to_use=None, ignored_row=0,
                  col_to_read=1, output_file=None, verbose=0):
    """
    Compute the false nearests fraction.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    min_dim : integer
        Minimal embedding dimension (Default to 1)
    max_dim : integer
        Maximale embedding dimension (Default to 5)
    comp_nmb : integer
        Number of components read from file (Default to 1)
    delay : integer
        Delay (Default to 1)
    ratio : number
        Ratio factor (Default to 2.0)
    theiler_wind : integer
        Theiler window (Default to 0)
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
    res : array
        first column: the dimension (counted like shown above)
        second column: the fraction of false nearest neighbors
        third column: the average size of the neighborhood
        fourth column: the average of the squared size of the neighborhood

    Note
    ----
    We implemented a new second criterion.
    If the distance to the nearest neighbor becomes smaller than the standard
    deviation of the data devided by the threshold, the point is omitted. This
    turns out to be a stricter criterion, but can show the effect that for
    increasing embedding dimensions the number of points which enter the
    statistics is so small, that the whole statistics is meanlingless.
    Be aware of this!
    """
    # prepare arguments
    args = "-x{} -c{} -m{} -M{},{} -d{} -f{} -t{} -V{}" \
           .format(ignored_row, col_to_read, min_dim, comp_nmb, max_dim,
                   delay, ratio, theiler_wind, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('false_nearest', args, input_data=data,
                      output_file=output_file)
    # return
    if msg != "":
        print(msg)
    return res
