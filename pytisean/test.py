import sys
import pdb
sys.path.append(r"/home/muahah/Dev/")
import pytisean.generators as ptg
import pytisean.embedding as pte
import pytisean.utilities as ptu
import pytisean.lyapunov as ptl
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # # Plot stability map
    # plt.figure()
    # xs = []
    # ys = []
    # for a in np.linspace(0.5, 2, 500):
    #     tmp_xy = ptg.henon(200, a=a, b=0)
    #     xs.append([a]*len(tmp_xy[:, 0]))
    #     ys.append(tmp_xy[:, 0])
    # plt.plot(xs, ys, ls='none', color='k', marker=",")

    # Generate hennon map
    xy = ptg.henon(20000, a=1.9999, b=0.0)
    # xy = ptg.makenoise(xy, noise_level=2, gaussian=True)

    # # Get dealy embedding map
    # delay = pte.delay(xy, dimension=2, vector_delay=1)
    # delay2 = pte.delay(xy, dimension=2, vector_delay=2)
    # delay3 = pte.delay(xy, dimension=2, vector_delay=3)
    # delay4 = pte.delay(xy, dimension=2, vector_delay=4)
    # plt.figure()
    # plt.plot(delay[:, 1], delay[:, 0], color='k', ls='none', marker=',')
    # plt.plot(delay2[:, 1], delay2[:, 0], color='r', ls='none', marker=',')
    # plt.plot(delay3[:, 1], delay3[:, 0], color='m', ls='none', marker=',')
    # plt.plot(delay4[:, 1], delay4[:, 0], color='b', ls='none', marker=',')
    # plt.plot([-1, 1], [-1, 1], ls='-', color='k')
    # plt.plot([1, -1], [-1, 1], ls='-', color='k')
    # plt.title('The Henon map')
    # plt.xlabel(r'$x$')
    # plt.ylabel(r'$y$')
    # plt.show(block=False)

    # # plot histogramme
    # hist = ptu.histogram(xy, bins=100)
    # plt.figure()
    # plt.plot(hist[:, 0], hist[:, 1])
    # x = np.linspace(-1, 1, 1000)
    # y = .02/(np.pi * (1 - x**2)**.5)
    # plt.plot(x, y)
    # plt.show(block=False)

    # # Plot and prettyfi
    # taus = [1, 2, 3, 4]
    # fig1, axs = plt.subplots(2, 2)
    # for i, tau in enumerate(taus):
    #     plt.sca(axs.flat[i])
    #     plt.scatter(xy[:-2*tau, 0], xy[tau:-tau, 0], c=xy[2*tau:, 0], s=1,
    #                 linewidths=0)
    #     plt.title('Henon map with tau={}'.format(tau))
    #     plt.xlabel(r'$x$', fontsize=16)
    #     plt.ylabel(r'$x + {}$'.format(tau), fontsize=16)
    # plt.show(block=False)

    # get lyapunov exponents
    it1, lyap_k, nmb_pts = ptl.lyap_k(xy, nmb_it=20, output_file=r"/tmp/pytisean/test.dat")
    it2, lyap_r = ptl.lyap_r(xy, nmb_it=20)
    x = np.linspace(0, 10, 100)
    y = x*np.log(2.) - 8
    plt.figure()
    plt.plot(it1, lyap_k, color='k', marker='o', ls='none', ms=3)
    plt.plot(it2, lyap_r, color='r', marker='o', ls='none', ms=3)
    plt.plot(x, y, color='k')
    plt.show(block=False)


    # # TEST POPEN
    # xy = np.random.random((10, 2))
    # import Pytisean.tiseanwrapper as ptw
    # res, msg = ptw.tisean("delay", ['-l100'], xy)
    # print(res)
