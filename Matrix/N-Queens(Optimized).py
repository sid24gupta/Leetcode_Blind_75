# https://leetcode.com/problems/n-queens/
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

from typing import List, Dict


def isSafe(row: int, col: int, n: int, row_checker: Dict[int, str],
           upper_diagonal_checker: Dict[int, str], lower_diagonal_checker: Dict[int, str]):
    x = row
    y = col

    # check for row
    if row_checker.get(x, 0) == 'Q':
        return False

    # check for lower diagonal
    if lower_diagonal_checker.get(x + y, 0) == 'Q':
        return False

    # check for upper diagonal
    if upper_diagonal_checker.get(n - 1 + y - x, 0) == 'Q':
        return False

    return True


def addsolution(board: List[List[str]], answer: List[List[str]], n: int):
    v1 = []
    for i in range(n):
        temp = ""
        for j in range(n):
            temp += board[i][j]
        v1.append(temp)
    answer.append(v1)


def solve(column: int, board: List[List[str]], answer: List[List[str]], n: int, row_checker: Dict[int, str],
          upper_diagonal_checker: Dict[int, str], lower_diagonal_checker: Dict[int, str]):
    if column == n:
        addsolution(board, answer, n)
        return

    for i in range(n):
        if isSafe(i, column, n, row_checker, upper_diagonal_checker, lower_diagonal_checker):
            board[i][column] = 'Q'
            row_checker[i] = 'Q'
            lower_diagonal_checker[i + column] = 'Q'
            upper_diagonal_checker[n - 1 + column - i] = 'Q'
            solve(column + 1, board, answer, n, row_checker, upper_diagonal_checker, lower_diagonal_checker)
            board[i][column] = '.'
            row_checker[i] = '.'
            lower_diagonal_checker[i + column] = '.'
            upper_diagonal_checker[n - 1 + column - i] = '.'


def solveNQueens(n: int) -> List[List[str]]:
    row_checker = {}
    upper_diagonal_checker = {}
    lower_diagonal_checker = {}
    answer = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(0, board, answer, n, row_checker, upper_diagonal_checker, lower_diagonal_checker)
    return answer


n = 4
v1 = solveNQueens(n)
print(v1)
