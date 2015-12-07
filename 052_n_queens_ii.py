class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt = 0
        self.solve(n, 0, [])
        return self.cnt

    def solve(self, n, row, queens):
        if row == n:
            self.cnt += 1
            return

        for col in range(n):
            if self.is_valid(row, col, queens):
                queens.append((row, col))
                self.solve(n, row + 1, queens)
                queens.pop()

    def is_valid(self, row, col, queens):
        for mrow, mcol in queens:
            if mrow == row or mcol == col:
                return False
            if abs(mrow - row) == abs(mcol - col):
                return False
        return True
