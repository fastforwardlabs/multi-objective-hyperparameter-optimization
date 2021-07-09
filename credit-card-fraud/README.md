# Multi-objective hyperparameter optimization for credit card fraud

The `credit-card-fraud.ipynb` notebook demonstrates using [Optuna](https://optuna.org/) for multi-objective hyperparameter optimization on the [Credit Card Fraud dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud).

In multi-objective hyperparameter optimization, we seek to find the "Pareto frontier" of points representing optimal tradeoffs between multiple objectives. In this example, we trade off prediction latency with predictive performance. The class distribution is heavily imbalanced, so we measure performance with the area under the PR curve. The notebook compares a Bayesian optimization algorithm: maximizing the expected hypervolume increase (EHVI) using multi-objective tree-structured Parzen estimators (MOTPE), with good old random search.

To get set up:

1. Install dependencies with `pip install -r requirements.txt`.
2. Download the dataset (requires Kaggle authentication) at this [link](https://www.kaggle.com/mlg-ulb/creditcardfraud), and place it at `data/creditcard.csv`.
3. Run the notebook with your Jupyter environment of choice. (If not using an external Jupyter environment, go ahead and install one with `pip install jupyter`).

The notebook was developed against Python 3.8.
