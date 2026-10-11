
class Solution:
    def __init__(self):
        self.ans = []

    def isSafe(self, board, row, col):
        # Check the column
        for r in range(row, -1, -1):
            if board[r][col] == "Q":
                return False

        # Check the positive diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # Check the negative diagonal
        r, c = row, col
        while r >= 0 and c < len(board[0]):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True

    def nQueens(self, board, row, n):
        if row == n:
            self.ans.append(["".join(r) for r in board])
            return

        for col in range(n):
            if self.isSafe(board, row, col):
                board[row][col] = "Q"
                self.nQueens(board, row + 1, n)
                board[row][col] = "."

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.ans = []
        board = [["."] * n for _ in range(n)]
        self.nQueens(board, 0, n)
        return self.ans