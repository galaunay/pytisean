""" TISEAN Function wrappers
"""

import sys
from TiseanWrapper import tiseano, tiseanio
import numpy as np

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
    Return a Henon map

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
    """
    args = "-l{} -A{} -B{} -X{} -Y{} -x{} -V{}" \
        .format(pts_nmb, a, b, x0, y0, disc_transients, verbose).split(" ")
    if output_file is not None:
        args += "-o{}".format(output_file)
    res, msg = tiseano('henon', *args)
    print(msg)
    return res

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # Generate 5000 iterates of the henon map
    xy = henon(50000, a=1.35)

    # Plot and prettyfi
    fig1, ax1 = plt.subplots(1, 1)
    ax1.scatter(xy[:, 0], xy[:, 1], color='k', s=0.1)
    plt.title('The Henon map')
    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$y$', fontsize=16)
    plt.show()
