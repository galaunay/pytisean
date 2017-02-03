# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN Lyapunov exponents wrappers
"""

from ..tiseanwrapper import tisean

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def lyap_k(data, min_dim=2, max_dim=2, delay=1, min_neighbors=None,
           max_neighbors=None, nmb_scales=5, nmb_ref_points=None,
           nmb_it=50, theiler_window=0, nmb_data_to_use=None,
           ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Give an estimation of the largest Lyapunov exponent using the algorithm of
    Kantz.

    Parameters
    ----------
    data : array or string
        Data, can de an array or a filename.
    min_dim : integer
        Minimal embedding dimension to use (default 2).
    max_dim : integer
        Maximal embedding dimension to use (default 2).
        Will make loops with different values of m between 'min_dim' and 'max_dim'
    delay : integer
        Delay to use (default 1).
        Note: this is not the delay associated with the vector delay.
        This delay need to be small in order to follow the deviation increase.
    min_neighbors : integer
        Minimal length scale to search neighbors
        (default is data interval / 1000).
    max_neighbors : integer
        Maximal length scale to search neighbors
        (default is data interval / 100).
    nmb_scales : integer
        Number of length scales to use (default 5).
        Will make loop with different values of epsilon, the neighbour radius.
    nmb_ref_points : integer
        Number of reference points to use (default to all)
    nmb_it : integer
        Number of iterations in time (default 50).
    theiler_window : integer
        Theiler window (default to 0).
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
    nmb_it : integer
        Iterations numbers.
    Lyap : number
        Lyapunov exponents.
        Results for loops over epsilon on dimension are concatenated in this
        array.
    nmb_points : integer
        Number of points for which a neighborhodd with enough points was found.

    Note
    ----
    As the Lyapunov exponents are computed for each dimension and each scale,
    the resulting lists are of size 'nmb_it*(max_dim - min_dim + 1)*scales'.
    """
    # prepare arguments
    args = "-x{} -c{} -M{} -m{} -d{} -#{} -s{} -t{} -V{}" \
           .format(ignored_row, col_to_read, max_dim, min_dim, delay,
                   nmb_scales, nmb_it, theiler_window, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if min_neighbors is not None:
        args += " -r{}".format(min_neighbors)
    if max_neighbors is not None:
        args += " -R{}".format(max_neighbors)
    if nmb_ref_points is not None:
        args += " -n{}".format(nmb_ref_points)
    args = args.split(" ")
    # run command
    res, msg = tisean('lyap_k', args, input_data=data, output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res[:, 0], res[:, 1], res[:, 2]


def lyap_r(data, dim=2, delay=1, ignor_window=0, min_neighbors=None,
           nmb_it=50, nmb_data_to_use=None,
           ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Give an estimation of the largest Lyapunov exponent using the algorithm of
    Rosenstein et al.

    Parameters
    ----------
    data : array or string
        Data, can de an array or a filename.
    dim : integer
        Embedding dimension to use (default 2).
    delay : integer
        Delay to use (default 1).
    ignor_window : integer
        Window around the reference point which should be omitted
        (Default 0).
    min_neighbors : integer
        Minimal length scale to search neighbors
        (default is data interval / 1000).
    nmb_it : integer
        Number of iterations in time (default 50).
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
    nmb_it : integer
        Iterations numbers.
    Lyap : number
        Lyapunov exponents.

    Note
    ----
    The resulting lists are of size 'nmb_it'.
    """
    # prepare arguments
    args = "-x{} -c{} -m{} -d{} -t{} -s{} -V{}" \
           .format(ignored_row, col_to_read, dim, delay, ignor_window,
                   nmb_it, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if min_neighbors is not None:
        args += " -r{}".format(min_neighbors)
    args = args.split(" ")
    # run command
    res, msg = tisean('lyap_r', args, input_data=data, output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res[:, 0], res[:, 1]
