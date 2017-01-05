"""
TISEAN linear tools wrapper
"""

from ..tiseanwrapper import tisean

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def corr(data, nmb_corr=100, std_norm=True, nmb_data_to_use=None,
         ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Computes the autocorrelation of a scalar data set.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    nmb_corr : integer
        Number of correlations (default 100).
    std_norm : boolean
        Use normalization to standard deviation.
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
    xy : list of [x, y] tuples
        Autocorrelation of the timse series.
    """
    # prepare arguments
    args = "-D{} -x{} -c{} -V{}" \
           .format(nmb_corr, ignored_row, col_to_read, verbose)
    if not std_norm:
        args += " -n"
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('corr', args, input_data=data, output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res


def armodel(data, dim=1, order=5, it_steps=None, nmb_data_to_use=None,
            ignored_row=0, col_to_read=1, output_file=None, verbose=0):
    """
    Fits (by means of least squares) a simple autoregressive (AR) model to
    the possibly multivariate data.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
    dim : integer
        Dimension of the vector (dafault 1).
    order : integer
        Order of the model (default to 5).
    it_steps : integer
        Number of steps to iterate on (default to no iterations).
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
    res : list of numbers
        Residual or iterated time series if 'it_steps' is specified.
    """
    # prepare arguments
    args = "-m{} -p{} -x{} -c{} -V{}" \
           .format(dim, order, ignored_row, col_to_read, verbose)
    if it_steps is not None:
        args += " -s{}".format(it_steps)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('ar-model', args, input_data=data, output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res
