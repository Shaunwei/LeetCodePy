class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0, 0)
        return

    def solve(self, board, i, j):
        if i == 9:
            return True
        if j == 9:
            return self.solve(board, i + 1, 0)
        if board[i][j] != '.':
            return self.solve(board, i, j + 1)

        for val in xrange(1, 10):
            if self.is_valid(board, i, j, str(val)):
                board[i][j] = str(val)
                if self.solve(board, i, j + 1):
                    return True
                board[i][j] = '.'
        return False

    def is_valid(self, board, i, j, val):
        for k in xrange(9):
            if board[k][j] == val or board[i][k] == val:
                return False

        mi = i / 3 * 3
        mj = j / 3 * 3
        for x in range(3):
            for y in range(3):
                if board[mi + x][mj + y] == val:
                    return False
        return True

