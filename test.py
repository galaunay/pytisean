import sys
import Pytisean.generators as ptg
import numpy as np

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # Generate 5000 iterates of the henon map
    xy = ptg.lorenz(50000)

    # Plot and prettyfi
    fig1, ax1 = plt.subplots(1, 1)
    ax1.scatter(xy[:, 0], xy[:, 1], color='k', s=0.1)
    plt.title('The Henon map')
    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$y$', fontsize=16)
    plt.show()
