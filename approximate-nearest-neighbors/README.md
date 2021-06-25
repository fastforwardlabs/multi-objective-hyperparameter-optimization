# Approximate nearest neighbor search


The `approximate-nearest-neighbor.ipynb` notebook demonstrates using [Optuna](https://optuna.readthedocs.io/en/stable/index.html) for multi-objective hyperparameter optimization on three approximate nearest neighbor (ANN) search algorithms. To get started, install dependencies with `pip install -r requirements.txt` (also included as the first executable cell in the notebook), and run the notebook with your Jupyter environment of choice. 

Some of the ANN algorithms explored in this notebook take a considerable amount of time and memory at install. They also take a long time to train during hyperparameter optimization. We've provided estimates of cell run times within the notebook. While we encourage experimentation and exploration, we include saved results so that execution of each cell is not strictly required. 

### A note on data
This notebook makes use of a GloVe word embeddings dataset reformatted by the [ANN Benchmarks](https://github.com/erikbern/ann-benchmarks) repository, a project that provides tools, code, and data for performing comparative benchmarking between various approximate neareset neighbor algorithms. However, the ANN Benchmarks library is a heavy install, designed to provide a suite of Docker containers for benchmarking purposes. We do not wish to belabor the already lengthy install for this notebook so we have borrowed and gently modified their dataset fetching functionality, which we include as `ann_benchmarks_dataset.py`. The original can be found [here](https://github.com/erikbern/ann-benchmarks/blob/18ba39b6a4af1243b26bf5fedc6c5c7ced791d70/ann_benchmarks/datasets.py). 


The notebook was developed against Python 3.8.