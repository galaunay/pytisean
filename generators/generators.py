""" TISEAN generators wrappers
"""

from ..tiseanwrapper import tiseano, tiseanio

__author__ = "Gaby Launay"
__copyright__ = "Gaby Launay 2017"
__credits__ = "Rainer Hegger, Holger Kantz and Thomas Schreiber"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "gaby.launay@tutanota.com"
__status__ = "Development"


def henon(pts_nmb, a=1.4, b=0.3, x0=0, y0=0, disc_transients=10000,
          output_file=None, verbose=0):
    """
    Return a Henon map.

    Dynamical model :
    x(n+1) = 1- a*x(n)^2 + b*y(n)
    y(n+1) = x(n)

    Parameters
    ----------
    pts_nmb : integer
        Number of points (0 for infinite)
    a, b : numbers
        Henon parameters (default to respectively 1.4 and 0.3)
    x0, y0 : numbers
        Initial position (default to 0, 0)
    disc_transients : integer
        Number of transients discarted (default to 10000)
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
    # prepare args
    args = "-l{} -A{} -B{} -X{} -Y{} -x{} -V{}" \
        .format(pts_nmb, a, b, x0, y0, disc_transients, verbose).split(" ")
    if output_file is not None:
        args += "-o{}".format(output_file)
    # run command and print messages
    res, msg = tiseano('henon', *args)
    print(msg)
    # return
    if not output_file:
        return res


def ikeda(pts_nmb, a=0.4, b=6.0, c=0.9, Re0=0, Im0=0, disc_transients=10000,
          output_file=None, verbose=0):
    """
    Return a Ikeda map.


    Dynamical model:
                                       i*b
    z(n+1) = 1 + c*z(n)* exp( i*a - ---------- )
                                    1 + |z(n)|
    Parameters
    ----------
    pts_nmb : integer
        Number of points (0 for infinite)
    a, b, c : numbers
        Ikedaz parameters (default to respectively 0.4, 6.0 and 0.9)
    Re0, Im0 : numbers
        Initial complex value of z
    disc_transients : integer
        Number of transients discarted (default to 10000)
    output_file : string
        Output fiel path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    xy : list of [x, y] tuples
        Successive iterations of the Ikeda map.
    """
    # prepare arguments
    args = "-l{} -A{} -B{} -C{} -R{} -I{} -x{} -V{}" \
        .format(pts_nmb, a, b, c, Re0, Im0, disc_transients, verbose).split(" ")
    if output_file is not None:
        args += "-o{}".format(output_file)
    # run command and print messages
    res, msg = tiseano('ikeda', *args)
    print(msg)
    # return
    if not output_file:
        return res

def lorenz(pts_nmb, freq=100, dyn_noise=0, rho=28., sigma=10., beta=8./3.,
           disc_transients=10000, output_file=None, verbose=0):
    """
    Return a Lorenz map.

    Dynamical model:
    dx/dt = sigma*(y - x)
    dy/dt = x*(rho - z) - y
    dz/dt = x*y - beta*z

    Parameters
    ----------
    pts_nmb : integer
        Number of points (0 for infinite)
    freq : number
        Sampling points per unit time (default to 100)
    rho, sigma, beta : numbers
        Lorenz parameters (default to respectively 28, 10 and 8/3)
    disc_transients : integer
        Number of transients discarted (default to 10000)
    output_file : string
        Output fiel path.
        If None, do not write a file, just return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    xyz : array of [x, y, z] tuples
        Successive iterations of the Lorenz map.
    """
    # prepare arguments
    args = "-l{} -f{} -r{} -R{} -S{} -B{} -x{} -V{}" \
        .format(pts_nmb, freq, dyn_noise, rho, sigma, beta,
                disc_transients, verbose).split(" ")
    if output_file is not None:
        args += "-o{}".format(output_file)
    # run command and print messages
    res, msg = tiseano('lorenz', *args)
    print(msg)
    # return
    if not output_file:
        return res


def arrun(coefficients, pts_nmb, order=None, seed=0, disc_transients=10000,
          nmb_data_to_use=None, ignored_row=0, ignored_col=1, col_to_read=1,
          output_file=None, verbose=0):
    """
    Run an autoregressive model from given ai coefficients.

    Model:
    xn = a1*xn-1 + ... + ap*xn-p + noise.

    Parameters
    ----------
    coefficients : array or string
        Rms amplitude of the increments (can be an array or a file path).
    pts_nmb : integer
        Number of points (0 for infinite)
    order : integer
        Order of the AR-model (determined b the inut by default)
    seed : integer
        Seed for random numbers
    disc_transients : integer
        Number of transients discarted (default to 10000)
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
    x : list of [x] tuples
        Successive iterations of the autoregressive model.
    """
    raise Exception('Not working yet')
    # Pb with the input data

    # prepare arguments
    args = "-l{} -I{} -R{} -S{} -B{} -x{} -V{}" \
        .format(pts_nmb, order, seed, disc_transients, verbose).split(" ")
    if order is not None:
        args += "-p{}".format(order)
    if output_file is not None:
        args += "-o{}".format(output_file)
    if isinstance(coefficients, str):
        if nmb_data_to_use is not None:
            args += "-l{}".format(nmb_data_to_use)
        args += "-x{}".format(ignored_row)
        args += "-M{}".format(ignored_col)
        args += "-c{}".format(col_to_read)
    # run command and print messages
    if isinstance(coefficients, str):
        args += coefficients
        res, msg = tiseano('ar-run', *args)
    else:
        res, msg = tiseanio(coefficients, 'ar-run', *args)
    print(msg)
    # return
    if not output_file:
        return res


def makenoise(time_serie, noise_level=5, abs_noise_level=None,
              gaussian=None, seed=0, nmb_data_to_use=None, ignored_row=0,
              ignored_col=1, col_to_read=1, output_file=None, verbose=0):
    """
    Add noise to a time series.

    Parameters
    ----------
    time_serie : array or string
        Time serie to add noise on (can be an array or a file path).
    noise_level : number
        Noise level in percent (default to 5%).
    abs_noise_level : number
        Absolute noise level (default to no noise).
    gaussian : boolean
        If 'true', use gaussian noise instead of uniform noise.
    seed : integer
        Seed for random numbers.
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
        Output file path.
        If None, do not write a file, and return the map.
    verbose : integer
        Verbosity level (defaul to 0 for only fatal errors.

    Returns
    -------
    noisy_time_serie : array
        Noisy time serie.
    """
    # prepare arguments
    args = "-%{} -I{} -V{}" \
        .format(noise_level, seed, verbose).split(" ")
    if output_file is not None:
        args += "-o{}".format(output_file)
    if abs_noise_level is not None:
        args += "-r{}".format(abs_noise_level)
    if gaussian:
        args += "-g"
    if isinstance(time_serie, str):
        if nmb_data_to_use is not None:
            args += "-l{}".format(nmb_data_to_use)
        args += "-x{}".format(ignored_row)
        args += "-M{}".format(ignored_col)
        args += "-c{}".format(col_to_read)
    # run command
    if isinstance(time_serie, str):
        args += time_serie
        res, msg = tiseano('makenoise', *args)
    else:
        res, msg = tiseanio(time_serie, 'makenoise', *args)
    # return
    print(msg)
    if not output_file:
        return res
