# -*- coding: utf-8 -*-
#!/usr/env python3

""" TISEAN noise reduction methods
"""

from ..tiseanwrapper import tisean

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def ghkss(data, delay=1, nmb_comp=1, dim=5, dim_manifold=2,
          min_nmb_neigh=30, min_neigh_size=None, nmb_it=1,
          euclidean_metric=False, nmb_data_to_use=None,
          ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Perform This program performs a noise reduction as proposed in Grassberger
    et al. In principal, it performs a orthogonal projection onto a
    q-dimensional manifold using a special (tricky) metric. In case the
    -2 parameter is set, an euclidean metric is used. This is done in
    Cawley et al. as well as in Sauer and is sometimes useful for flow systems.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    delay : integer
        Delay for the delay vector (defaul to 1)
    nmb_comp : integer
        Number of components (default to 1).
    dim : integer
        Embedding dimension (default to 5).
    dim_manifold : integer
        Dimension of the manifold to project to (default to 2).
    min_nmb_neigh : integer
        Minimal number of neighbours (default to 30).
    min_neigh_size : number
        Minimal size of the neighbourhood (default 0.1% of the data interval)
    nmb_it : integer
        Number of iterations (defailt to 1)
    euclidean_metric : boolean
        If 'True', use the euclidean metric instead of the tricky one.
        (default to 'False')
    nmb_data_to_use : integer
        Number of data points to use (default to everything).
    ignored_row : integer
        Number of file rows to ignore if 'time_serie' is a file path
        (Default to 0).
    col_to_read : integer
        Number of columns to be read if 'time_serie' is a file path
        (Default to 1,...,nmb_comp).
    output_file : string
        Output fiel path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    filt_data : array
        Filtered data.
        (Additional information are avaialable as comments in the result file)

    """
    # prepare arguments
    args = "-x{} -m{},{} -d{} -q{} -k{} -i{} -V{}"\
           .format(ignored_row, nmb_comp, dim, delay, dim_manifold,
                   min_nmb_neigh, nmb_it, verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if col_to_read is not None:
        args += " -c{}".format(col_to_read)
    if min_neigh_size is not None:
        args += " -r{}".format(min_neigh_size)
    if euclidean_metric:
        args += " -2"
    args = args.split(" ")
    # run command
    res, msg = tisean('ghkss', args, input_data=data, output_file=output_file)
    # return
    if msg != "":
        print(msg)
    if not output_file:
        return res
