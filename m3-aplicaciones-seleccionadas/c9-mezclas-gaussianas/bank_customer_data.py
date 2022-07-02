from scipy.stats import multivariate_normal
import pandas as pd
import numpy as np


def generate_bank_customer_data(n_common=200, n_debtors=150, n_good=50, include_labels=True):
    """
    Function to generate bank customers data characterized by income and debt.
    :param int n_common: Number of common customers.
    :param int n_debtors: Number of debtors.
    :param int n_good: Number of good customers.
    :param bool include_labels: Whether to include or not ground truth labels.
    :return: pd.DataFrame with generated data.
    """
    # Parameters
    mu1 = np.array([3, 2.5])
    mu2 = np.array([2, 6])
    mu3 = np.array([6, 5])
    cov1 = np.array([[1.2, -0.2],
                     [-0.2, 1]])
    cov2 = np.array([[0.6, 0],
                     [0, 0.6]])
    cov3 = np.array([[1, 0.9],
                     [0.9, 1]])
                     
    # Ground truth random variables
    p1 = multivariate_normal(mean=mu1, cov=cov1)
    p2 = multivariate_normal(mean=mu2, cov=cov2)
    p3 = multivariate_normal(mean=mu3, cov=cov3)
    
    # Data generation
    data = np.concatenate([p1.rvs(size=n_common), 
                           p2.rvs(size=n_debtors),
                           p3.rvs(size=n_good)],
                          axis=0)
    data = pd.DataFrame({"income": data[:, 0], "debt": data[:, 1]})
    
    # Include ground truth labels
    if include_labels:
        data["labels"] = np.concatenate([np.zeros((n_common, 1)), 
                                         np.ones((n_debtors, 1)), 
                                         2 * np.ones((n_good, 1))],
                                        axis=0)
   
    return data.sample(frac=1).reset_index(drop=True)
