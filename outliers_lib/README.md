# Statistical methods for finding outliers

## Defenition of outlier

***Outlier (anomaly)*** - is an observation that is significantly out of the general distribution and very different from other data.

This section discusses statistical methods for finding outliers, namely:
* Interquartile range method 
* The z-differences method (sigma method)

## Interquartile range method

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Boxplot_vs_PDF.svg/1200px-Boxplot_vs_PDF.svg.png)

### Method algorithm:

1. Calculate the 25th and 75th quantiles (1st and 3rd quartiles) - $Q_{25}$ and $Q_{75}$ of thr examining frature
2. Calculate interquartile distance:
     * $IQR=Q_{75}-Q_{25}$
3. Determine the upper and lower Tukey bounds:

     * $bound_{upper} = Q_{75} + 1.5*IQR$
    
     * $bound_{lower} = Q_{25} - 1.5*IQR$
4. Find observations that are out of bounds


The method requires that the feature, on the basis of which the outlier search is performed, be normally distributed.

We can try to use data transformation methods, as taking logarithms, to try to reduce the distribution to normal, or at least to symmetrical.

We also can add variability to the number of quartile ranges on the left and right sides of the distributions.


## Z-score method (sigma method)

The three sigma rule: if the data distribution is normal, then 99.73% lie in the interval: $(\mu-3 \sigma$ , $\mu+3 \sigma)$,
where
* $\mu$ - mathematical expectation (for the sample, this is the average value)
* $\sigma$ - standard deviation.

Observations that lie outside this interval will be considered outliers.
![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Empirical_rule_histogram.svg/450px-Empirical_rule_histogram.svg.png)

### Method algorithm:

1. Calculate the mean and standard deviation of $\mu$ and $\sigma$ for the feature we are examining
2. Define upper and lower bounds:
     * $bound_{upper} = \mu - 3 * \sigma$
    
     * $bound_{lower} = \mu + 3 * \sigma$
3. Find observations that are out of bounds


The method requires that the feature, on the basis of which the outlier search is performed, be normally distributed.


We can use data transformation methods, such as taking logarithms, to try to reduce the distribution to normal, or at least to symmetrical.

We can also add variance to the number of standard deviations to the left and right sides of the distributions.

## Method Implementation

The methods are implemented as find_outliers_iqr() and find_outliers_z_score() functions. The functions are provided in the find_outliers.py file. Documentation provided for functions.

## Usage example

Mandatory arguments of the functions that implement outlier search methods are:
* data(pandas.DataFrame): dataset (table)
* feature (str): name of the feature based on which outliers are searched

Using classical approaches without modifications:
```python
# Interquartile range method
from outliers_lib.find_outliers import find_outliers_iqr

outliers_iqr, cleaned_iqr = find_outliers_iqr(data, feature)

# Z-score method (sigma method)
from outliers_lib.find_outliers import find_outliers_z_score

find_outliers_z_score
outliers_z_score, cleaned_z_score = find_outliers_z_score(data, feature)
```
Using methods with pre-logarithm:
```python
outliers_iqr, cleaned_iqr = find_outliers_iqr(data, feature, log=True)
outliers_z_score, cleaned_z_score = find_outliers_z_score(data, feature, log=True)
```
Using methods with pre-logarithm and adding scatter variance:
```python
outliers_iqr, cleaned_iqr = find_outliers_iqr(data, feature, log=True, left=2, right=2)
outliers_z_score, cleaned_z_score = find_outliers_z_score(data, feature, log=True, left=2, right=2)
```


## Used tools and libraries
* numpy (1.23.2)
* pandas (1.4.4)

## Additional sources:
* [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
* [Interquartile range method](https://en.wikipedia.org/wiki/Interquartile_range)
* [Three sigma rule](https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule)



