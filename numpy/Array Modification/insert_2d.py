import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

new_arr_2d = np.insert(arr_2d, 1, [10, 11,12],axis=0) # insert a new row at index 1
print(new_arr_2d) # new 2D array with inserted row