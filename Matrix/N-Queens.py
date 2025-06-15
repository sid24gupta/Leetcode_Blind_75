# https://leetcode.com/problems/n-queens/
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

from typing import List


def isSafe(row: int, column: int, board: List[List[str]])-> bool:

    # check row
    x = row
    y = column
    while y >= 0:
        if board[x][y] == 'Q':
            return False
        y -= 1
    # check lower diagonal
    x = row
    y = column
    while y >=0 and x < n:
        if board[x][y] == 'Q':
            return False
        x += 1
        y-= 1

    # check upper diagonal
    x = row
    y = column
    while x >= 0 and y >= 0:
        if board[x][y] == 'Q':
            return False
        x -= 1
        y -= 1

    return True
def addanswer(board: List[List[str]], ans: List[List[str]], n:int):

    temp = []
    for i in range(n):
        t1 = ""
        for j in range(n):
            t1 += board[i][j]
        temp.append(t1)
    ans.append(temp)
def solve(column: int, board: List[List[str]], ans: List[List[str]], n:int ):

    if column == n:
        addanswer(board,ans,n)
        return

    for i in range(n):
        if isSafe(i,column,board):
            board[i][column] = 'Q'
            solve(column+1, board, ans, n)
            board[i][column] = '.'

def solveNQueens(n: int) -> List[List[str]]:

    answer = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(0,board,answer,n)
    return answer


n = 4
v1 = solveNQueens(n)
print(v1)