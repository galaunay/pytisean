""" TISEAN utilities wrappers
"""

from ..tiseanwrapper import tisean

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def histogram(data, bins=50, nmb_data_to_use=None, ignored_row=0,
              col_to_read=1, output_file=None, verbose=0):
    """
    Estimate the scalar distribution of a scalar set.

    Parameters
    ----------
    data : array or string
        data, can de an array or a filename.
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
    xy : list of [x, y] tuples
        With 'x' the bin position and 'y' the bin value.
    """
    # prepare arguments
    args = "-x{} -c{} -b{} -V{}" \
           .format(ignored_row, col_to_read, bins, verbose)
    if nmb_data_to_use is not None:
        args += "-l{}".format(nmb_data_to_use)
    args = args.split(" ")
    # run command
    res, msg = tisean('histogram', args, input_data=data,
                      output_file=output_file)
    # return
    print(msg)
    if not output_file:
        return res
