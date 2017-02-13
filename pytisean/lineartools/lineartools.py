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
    if msg != "":
        print(msg)
    if not output_file:
        return res


def ar_model(data, dim=1, order=5, it_steps=None, nmb_data_to_use=None,
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
    if msg != "":
        print(msg)
    if not output_file:
        return res


def ar_run(data, nmb_it, order=None, seed=None, nmb_trans=10000,
            output_file=None, verbose=0):
    """
    Compute iterates of an autoregressive model.

    Parameters
    ----------
    nmb_it : integer
        Number of iterations.
    order : integer
        Order of the AR-model (default is determined by input)
    seed : integer
        Seed for random numbers.
    nmb_trans : integer
        Number of discarted transients (default to 10000).
    output_file : string
        Output file path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    Successice values of the AR-model
    """
    # prepare arguments
    args = "-l{} -x{} -V{}" \
           .format(nmb_it, nmb_trans, verbose)
    if order is not None:
        args += " -p{}".format(order)
    if seed is not None:
        args += " -I{}".format(seed)
    args = args.split(" ")
    # run command
    res, msg = tisean('ar-run', args, input_data=data,
                      output_file=output_file)
    # return
    if msg != "":
        print(msg)
    if not output_file:
        return res


def pca(data, dim=1, delay=1, output='eigenvalues', modes_to_keep=None,
        nmb_data_to_use=None, ignored_row=0, col_to_read=1, output_file=None,
        verbose=0):
    """
    Performs a global principal component analysis (PCA).
    It gives the eigenvalues of the covariance matrix and depending
    on the 'output' value, eigenvectors, projections...
    of the input time series.

    Parameters
    ----------
    data : array or string
        Data, can de an array or a filename.
    dim : integer
        Embedding dimension
        (Should be at least '2*modes_to_keep' for filtering)
    delay : integer
        Time delay
    output : string in {'eigenvalues', 'eigenvectors', 'transformation',
                        'truncated'}
       Output values : 'eigenvalues': Just write the eigenvalues
                       'eigenvectors': Write the eigenvectors
                       'transformation': Transformation of the time series
                       onto the eigenvector basis.
                       'truncated': Project the time series onto the first -q
                       eigenvectors (global noise reduction).
    modes_to_keep : integer
        Number of modes to keep (for 'output'='transformation' or ' truncated')
        Default to all (should be at least the signal embedding dimension).
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
    Depends on the 'output' value.

    """
    # prepare
    arg_W = {'eigenvalues': 0, 'eigenvectors': 1, 'transformation': 2,
             'truncated': 3}
    # prepare arguments
    args = "-x{} -c{} -m{},{} -d{} -W{} -V{}"\
           .format(ignored_row, col_to_read, col_to_read, dim, delay, arg_W[output],
                   verbose)
    if nmb_data_to_use is not None:
        args += " -l{}".format(nmb_data_to_use)
    if modes_to_keep is not None:
        args += " -q{}".format(modes_to_keep)
    args = args.split(" ")
    # run command
    res, msg = tisean('pca', args, input_data=data, output_file=output_file)
    # return
    if msg != "":
        print(msg)
    if not output_file:
        return res
