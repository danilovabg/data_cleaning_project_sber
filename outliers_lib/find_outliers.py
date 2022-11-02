import numpy as np
import pandas as pd

def find_outliers_iqr(data, feature, left=1.5, right=1.5, log_scale=False):
    """
    Finds outliers in data using the interquartile range method.
        The classic method is modified by adding:
        * Possibility of logarithm distribution
        * manual control of the number of interquartile ranges on both directions of the distribution
        Args:
            data(pandas.DataFrame): dataset
            feature (str): name of the feature based on searchng outliers
            left (float, optional): number of interquartile ranges to the left of the distribution. The default is 1.5.
            right (float, optional): number of interquartile ranges to the right side of the distribution. The default is 1.5.
            log_scale (bool, optional): logarithm mode. Default is False - no logarithm is applied.

        returns:
            pandas.DataFrame: outlier observations
            pandas.DataFrame: cleaned data with removed outliers
    """
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x= data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x<lower_bound) | (x > upper_bound)]
    cleaned = data[(x>lower_bound) & (x < upper_bound)]
    return outliers, cleaned

def find_outliers_z_score(data, feature, left=3, right=3, log_scale=False):
    """
    Finds outliers in data using the z-deviation method.
    The classic method is modified by adding:
    * Possibility of logarithm distribution
    * manual control of the number of standard deviations on both sides of the distribution
    Args:
        data(pandas.DataFrame): dataset
        feature (str): name of the feature based on which outliers are searched
        left (float, optional): number of standard deviations to the left of the distribution. The default is 1.5.
        right (float, optional): number of standard to the right side of the distribution. The default is 1.5.
        log_scale (bool, optional): logarithm mode. Default is False - no logarithm is applied.

    returns:
        pandas.DataFrame: outlier observations
        pandas.DataFrame: cleaned data with removed outliers 
    """
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x = data[feature]
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left * sigma
    upper_bound = mu + right * sigma
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned

