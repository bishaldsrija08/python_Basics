# Fancy indexing is a term used to describe the use of arrays of integers or boolean values to index into another array. It allows you to select specific elements from an array based on their positions or conditions.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[[0, 2, 4]])  # Output: [10 30 50]