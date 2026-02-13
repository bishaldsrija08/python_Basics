# ndim of numpy array
import numpy as np
arr_3d = np.array([[[1, 2, 3],
                     [4, 5, 6]],
                    [[7, 8, 9],
                     [10, 11, 12]]])
print(arr_3d.ndim)  # Output: 3


arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d.ndim)  # Output: 1