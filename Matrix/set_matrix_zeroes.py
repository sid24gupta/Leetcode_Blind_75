# https://leetcode.com/problems/set-matrix-zeroes/description/
# 73. Set Matrix Zeroes
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
from typing import List 

def setZeroes(matrix: List[List[int]]) -> List[List]:

    visited = []

    for i in range(len(matrix)):
        t = []
        for j in range(len(matrix[0])):
            t.append(0)
        visited.append(t)

    list_check_for_i = set()
    list_check_for_j = set()

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):

            if matrix[i][j] == 0:
                list_check_for_i.add(i)
                list_check_for_j.add(j)

    list_check_for_i = list(list_check_for_i)
    list_check_for_j = list(list_check_for_j)

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):

            if (i in list_check_for_i or j in list_check_for_j) and visited[i][j]==0:
                matrix[i][j] = 0
                visited[i][j] = 1

    
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
v1 = setZeroes(matrix)
print(matrix)