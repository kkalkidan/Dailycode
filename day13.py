"""
@Question 
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

"""
import numpy as np

def rotate_90(arr):

    arr_temp = np.array(arr).flatten()
    result = np.zeros((len(arr), len(arr)))

    a = 2 * len(arr)
    b = len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            result[i][j] = arr_temp[(a + j) - (b * i)]

    return result


print(rotate_90([[1, 2, 3],[4, 5, 6], [7, 8, 9]]))

"""
@Solution 

next:  in place rotation

For an NxN array
90deg rotation = ((2*sizeofarray) + j) - (sizeofarray* i))
"""

