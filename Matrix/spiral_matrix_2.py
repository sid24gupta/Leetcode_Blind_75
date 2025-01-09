# https://leetcode.com/problems/spiral-matrix-ii/description/
# 59. Spiral Matrix II
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

from typing import List

def generateMatrix(n: int) -> List[List[int]]:

    matrix = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(0)
        matrix.append(t)
    
    counter = 1

    left , right = 0 , len(matrix[0])
    top , bottom = 0 , len(matrix)

    while left < right and top < bottom:

        for i in range(left,right):
            matrix[top][i] = counter
            counter += 1
        top += 1
        
        for i in range(top,bottom):
            matrix[i][right-1] = counter
            counter += 1
        right -= 1

        if not(left < right and top < bottom):
            break

        for i in range(right-1,left-1,-1):
            matrix[bottom-1][i] = counter
            counter += 1
        bottom -= 1
        
        for i in range(bottom-1,top-1,-1):
            matrix[i][left] = counter
            counter += 1
        left += 1

    return matrix

n = 3
v1 = generateMatrix(n)
print(v1)