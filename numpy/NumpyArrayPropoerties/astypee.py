# astype in numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr_float = arr.astype(float)
print(arr_float)  # Output: [1. 2. 3. 4. 5.]

arr_float = np.array([1.5, 2.5, 3.5, 7.8])
arr_int_converted = arr_float.astype(int)
print(arr_int_converted)  # Output: [1 2 3]