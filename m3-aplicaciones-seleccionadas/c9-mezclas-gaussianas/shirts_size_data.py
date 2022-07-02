from scipy.stats.distributions import norm
import pandas as pd
import numpy as np


def generate_shirts_data(n_small=50, n_large=60, include_labels=True):
    """
    Function to generate t-shirts data characterized by their size.
    :param int n_small: Number of small shirts.
    :param int n_large: Number of large shirts.
    :param bool include_labels: Whether to include or not ground truth labels.
    :return: pd.DataFrame with generated data.
    """
    # Parameters
    mu1 = 30
    mu2 = 40
    s1 = 2
    s2 = 3
                     
    # Ground truth random variables
    p1 = norm(loc=mu1, scale=s1)
    p2 = norm(loc=mu2, scale=s2)
    
    # Data generation
    data = np.concatenate([p1.rvs(size=n_small).reshape((-1,)), 
                           p2.rvs(size=n_large).reshape((-1,))])
    data = pd.DataFrame({"size": data})
    
    # Include ground truth labels
    if include_labels:
        data["labels"] = np.concatenate([np.zeros((n_small, 1)), 
                                         np.ones((n_large, 1))],
                                        axis=0)
   
    return data.sample(frac=1).reset_index(drop=True)
