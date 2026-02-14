"""
.ravel() is used to flatten a multi-dimensional array into a 1D array. It returns a contiguous flattened array. The original array is not modified, and the flattened array is a view of the original array. This means that any changes made to the flattened array will affect the original array.

.flatten() is also used to flatten a multi-dimensional array into a 1D array. However, it returns a copy of the original array, which means that any changes made to the flattened array will not affect the original array. In summary, .ravel() returns a view of the original array, while .flatten() returns a copy of the original array.

"""
import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])
flattened_arr_ravel = arr_2d.ravel()
print(flattened_arr_ravel)
flattened_arr_flatten = arr_2d.flatten()
print(flattened_arr_flatten)