import pdb
import sys
import os
sys.path.append(r"/home/muahah/Dev/pytisean")
import pytisean.generators as ptg
import pytisean.embedding as pte
import pytisean.utilities as ptu
import pytisean.lyapunov as ptl
import pytisean.lineartools as ptlt
import numpy as np
import matplotlib.pyplot as plt

# Import data
try:
    os.chdir(os.path.dirname(__file__))
except NameError:
    pass
msg, data = ptu.import_data_file("amplitude.dat")
print(msg)

# Plot data
plt.figure()
plt.plot(data, 'k', lw=1)
plt.title("Data")
plt.show(block=False)

# Get and plot correlation
corr = ptlt.corr(data)
plt.figure()
plt.plot(corr[:, 0], corr[:, 1], 'k', lw=1)
plt.title("Autocorrelation")
plt.show(block=False)

# Get the AR model
x = range(len(data))
res1 = ptlt.armodel(data, order=10)
res2 = ptlt.armodel(data, order=50)
plt.figure()
plt.plot(data, 'k', lw=1, label="Original data")
plt.plot(x[10::], res1, 'b', lw=1, label="Residual with order 10 model")
plt.plot(x[50::], res2, 'r', lw=1, label="Residual with order 50 model")
plt.legend()
plt.show(block=False)

# Compare histograms
x = range(len(data))
fit = ptlt.armodel(data, order=10, it_steps=50000)
hist1 = ptu.histogram(data, bins=50)
hist2 = ptu.histogram(fit, bins=50)
plt.figure()
plt.plot(hist1[:, 0], hist1[:, 1], 'k', lw=1, label="Original data histogram")
plt.plot(hist2[:, 0], hist2[:, 1], 'r', lw=1, label="Fit (order 10) histogram")
plt.legend()
plt.show(block=False)

# Compare autocorrelation and spectra
# TODO :
