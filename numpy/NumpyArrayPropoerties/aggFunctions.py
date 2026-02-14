# Aggregate functions in NumPy are used to perform operations on arrays and return a single value. These functions include sum, mean, median, standard deviation, minimum, maximum, and variance. Here is an example of how to use these aggregate functions with a NumPy array:

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Variance:", np.var(arr))