# https://leetcode.com/problems/spiral-matrix/description/
# 54. Spiral Matrix
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:

    left , right = 0 , len(matrix[0])
    top , bottom = 0 , len(matrix)
    answer = []

    while left < right and top < bottom:

        for i in range(left,right):
            answer.append(matrix[top][i])
        top += 1

        for i in range(top,bottom):
            answer.append(matrix[i][right-1])
        right -= 1

        if not (left<right and top<bottom):
            break

        for i in range(right-1,left-1,-1):
            answer.append(matrix[bottom-1][i])
        bottom -= 1

        for i in range(bottom-1,top-1,-1):
            answer.append(matrix[i][left])
        left += 1

    return answer 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
v1 = spiralOrder(matrix)
print(v1)