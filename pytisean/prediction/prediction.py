# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN prediction tools wrappers
"""

from ..tiseanwrapper import tisean

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def lzo_test(data, dim=2, delay=1, nmb_comp=1, nmb_error=None,
             dist_ref=1, min_nmb_neigh=30, neigh_init_size=None,
             neigh_incr_factor=1.2, forecasted_steps=1,
             caus_win_size=None, nmb_data_to_use=None,
             ignored_row=0, col_to_read=None,
             output_file=None, verbose=0):
    """
    Compute the forecasting error using a zeroth order NL model.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    dim : integer
        Embedding dimension (default to 2).
    delay : integer
        Embedding delay (default to 1).
        Should not necessarily be the embedding dimension.
    nmb_comp : integer
        Number of components of the time serie (default to 1).
    nmb_error : integer
        Number of points where error should be computed (default to all).
    dist_ref : integer
        Temporal distance between the reference points (default to 1).
    min_nmb_neigh : integer
        Minimal number of neighbors for the fit (default to 30).
    neigh_init_size : number
        Neighborhood size to start with (default to 0.1% of the data interval).
    neigh_incr_factor : number
        Factor to increase the neighborhood size if not enough neighbors were
        found (default to 1.2).
    forecasted_steps : integer
        Step to be forecasted (default to 1).
        Function return one line for each tested steps, from 1 to
        'forecasted_steps'.
    caus_win_size : integer
        Width of the causality window (default to the same value as
        'forecasted_steps').
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'data' is a file path
        (Default to 0).
    col_to_read : integer
        Number of columns to be read if 'data' is a file path
        (Default to 1).
    output_file : string
        Output field path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    res : array
       First column : forecasted steps.
       Following columns : relative forecast errors.
       As many lines as 'forecasted_steps'
    """
    # prepare arguments
    args = "-x{} -m{},{} -d{} -S{} -k{} -f{} -s{} -V{}" \
           .format(ignored_row, nmb_comp, dim, delay, dist_ref, min_nmb_neigh,
                   neigh_incr_factor, forecasted_steps, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if col_to_read is not None:
        args += " -c{}".format(col_to_read)
    if nmb_error is not None:
        args += " -n{}".format(nmb_error)
    if neigh_init_size is not None:
        args += " -r{}".format(neigh_init_size)
    if caus_win_size is not None:
        args += " -C{}".format(caus_win_size)
    args = args.split(" ")
    # run command
    res, msg = tisean('lzo-test', args, input_data=data,
                      output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res
