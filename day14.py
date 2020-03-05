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

def rotate_90(array):
    N = len(array)
    for i in range(N//2):
        for j in range(N-i-1):
            temp = array[i][j]
            array[i][j] = array[N-1-j][i]
            array[N-1-j][i] = array[N-1-i][N-1-j]
            array[N-1-i][N-1-j] = array[j][N-1-i]
            array[j][N-1-i] = temp
      
    return array

print(rotate_90([[1, 2, 3],[4, 5, 6], [7, 8, 9]]))

"""
@Solution 

in place rotation

https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

"""

