# dtype of numpy array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # Output: int64 (or int32 depending on the system)

arr_float = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(arr_float.dtype)  # Output: float64 (or float32 depending on the system)

arr_str = np.array(['a', 'b', 'c', 'd', 'e'])
print(arr_str.dtype)  # Output: <U1 (or <U depending on the system)

arr_names = np.array(['Alice', 'Bob', 'Charlie'])
print(arr_names.dtype)  # Output: <U7 (or <U depending on the system)