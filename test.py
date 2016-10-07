import sys
import pdb
sys.path.append(r"/home/glaunay/Freecom/These/Modules_Python")
import Pytisean.generators as ptg
import Pytisean.embedding as pte
import numpy as np

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # Generate 5000 iterates of the henon map
    xy = ptg.henon(5000)

    # # Plot and prettyfi
    # fig1, ax1 = plt.subplots(1, 1)
    # ax1.scatter(xy[:, 0], xy[:, 1], color='k', s=0.1)
    # plt.title('The Henon map')
    # plt.xlabel(r'$x$', fontsize=16)
    # plt.ylabel(r'$y$', fontsize=16)
    # plt.show(block=False)

    # Get temporal embedding

    # # Get delay
    # tau = pte.delay(xy, 2)
    # print("Delay = {}".format(tau))



    # TEST POPEN
    xy = np.random.random((10, 10))
    import Pytisean.tiseanwrapper as ptw
    res = ptw.tisean("delay", args=['-m2', '-d1', '-V0'], input_data=xy)
    print(res)
