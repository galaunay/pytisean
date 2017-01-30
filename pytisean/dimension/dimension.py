# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN dimension estimator tools wrappers
"""

from ..tiseanwrapper import tisean

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def d2(data, delay=1, min_dim=1, max_dim=10, theiler_wind=0,
       min_len_scale=None, max_len_scale=None, nmb_eps=100,
       max_nmb_pair=1000, normalized_data=False, nmb_data_to_use=None,
       ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Estimate the correlation sum, the correlation sum slope and the
    correlation entropie, used to get the correlation dimension.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    delay : integer
        Delay for the delay vector (defaul to 1)
    min_dim : integer
        Minimum embedding dimension (default to 1).
    max_dim : integer
        Maximum embedding dimension (default to 10).
    theiler_wind : integer
        Theiler window (default to 0)
    min_len_scale : integer
        Minimal length scale (default to 1/1000 of the data length)
    max_len_scale : integer
        Maximum length scale (default to the data length)
    nmb_eps : integer
        Number of epsilon values (default to 100)
    max_nmb_pair : integer
        Maximum number of pairs to use (default to 1000).
        0 means all possible pairs.
    normalized_data : boolean
        Use data that is normalized to [0, 1] for all components
        (default to False)
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
    c2 : 2xn array
        Correlation sum
    d2 : 2xn array
        Correlation sum slope
    h2 : 2xn array
        Entropies
    """
    # prepare arguments
    args = "-x{} -d{} -M{},{} -c{} -t{} -#{} -N{} -V{}"\
           .format(ignored_row, delay, min_dim, max_dim, col_to_read,
                   theiler_wind, nmb_eps, max_nmb_pair, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if min_len_scale is not None:
        args += " -r{}".format(min_len_scale)
    if max_len_scale is not None:
        args += " -R{}".format(max_len_scale)
    if normalized_data:
        args += " -E"
    args = args.split(" ")
    # run command
    res, msg = tisean('d2', args, input_data=data, output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res
