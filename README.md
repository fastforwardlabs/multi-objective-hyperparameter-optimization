# Multi-objective hyperparameter optimization


This repo accompanies Cloudera Fast Forward Labs report [Multi-objective hyperparameter optimization (aka random search is all you need)] (LINK).  It contains tutorials and experimentation for applying multi-objective optimization (MOO) to hyperparameter optimization (HPO) for machine learning models. Each of the directories in the repository contain a stand-alone experiment, formatted as Jupyter Notebook style blog post. We describe each in brief below, and additional details can be found within the corresponding directory.  

1. `ax-on-synthetic-data` contains a minimal example of MOO of a simple multi-layer perceptron model on a synthetic dataset generated by scikit-learn using the Ax optimization library. 
2. `optuna-on-synethic-data` of a simple multi-layer perceptron model on a synthetic dataset generated by scikit-learn using the Optuna hyperparameter optimization library. 
3. `credit-card-fraud` contains a notebook that walks through an application of Optuna for multi-objective optimization on a credit card fraud dataset using an XGBoost model. 
3. `approximate-nearest-neighbors` contains a notebook that applies Optuna for MOO on three approximate nearest neighbor algorithms -- Annoy, Hierarchical Navigable Small Worlds, and Locality Sensitive Hashing -- each trained on GloVe word embeddings. 
