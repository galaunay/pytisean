# pytisean
Tisean library python wrapper.

## Introduction
High-level python functions to interact with the [Tisean](http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/index.html) library.
Those functions can work with file, if you specify the input and ouput files (like Tisean does), or with python data.
Some Tisean commands are still not avalaible (see [Available commands](#available-commands)).

## Installation
### Tisean library
You need to install the Tisean library, not included in this package, and avalaible [here](http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/index.html).
The Tisean binaries need to be on your $PATH.
### Package

## Basic usage
### Available commands
Available commands are for the moment:
- Generators (5/5):
  - `henon`
  - `ikeda`
  - `lorenz`
  - `ar-run`
  - `makenoise`
- Linear tools (3/10):
  - `ar-run`
  - `corr`
  - `pca`
- Utilities (1/5):
  - `histogram`
- Stationarity (2/3):
  - `recurr`
  - `stop`
- Embedding (2/7):
  - `delay`
  - `mutual`
  - `flase_nearest`
- Prediction (0/11):
- Noise reduction (0/4):
- Dimension and entropy (0/7):
- Lyapunov exponents (2/3):
  - `lyap_k`
  - `lyap_r`
- Surrogate (0/5):
- Spike trains (0/6):
- XTisean (0/4):

### Tiseanwrapper
Even without dedicated python functions, `tiseanwrapper.tisean()` allow to launch any Tisean command in a lower level.
