# -*- coding: utf-8 -*-
#!/usr/env python3

import sys
import pdb
sys.path.append(r"/home/glaunay/.local/bin")
import Pytisean.generators as ptg
import Pytisean.embedding as pte
import numpy as np

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # Generate 5000 iterates of the henon map
    xy = ptg.henon(5000)

    # Plot and prettyfi
    fig1, ax1 = plt.subplots(1, 1)
    ax1.scatter(xy[:, 0], xy[:, 1], color='k', s=0.1)
    plt.title('The Henon map')
    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$y$', fontsize=16)
    plt.show(block=False)

    # Get temporal embedding
    # Get delay
    tau = pte.delay(xy, 2)
    print("Delay =\n{}".format(tau))



    # # TEST POPEN
    # xy = np.random.random((10, 2))
    # import Pytisean.tiseanwrapper as ptw
    # res, msg = ptw.tisean("delay", ['-l100'], xy)
    # print(res)
