class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        5:25 - 5:37
        """
        ret = []
        self.solve(n, 0, ret, [])
        return ret

    def solve(self, n, i, ret, queens):
        if i == n:
            ret.append(self.build(n, queens))
            return

        for j in range(n):
            if self.is_valid(i, j, queens):
                queens.append((i, j))
                self.solve(n, i + 1, ret, queens)
                queens.pop()

    def is_valid(self, i, j, queens):
        for mi, mj in queens:
            if mi == i or mj == j:
                return False
            if abs(mi - i) == abs(mj - j):
                return False
        return True

    def build(self, n, queens):
        board = [['.' for _ in range(n)] for _ in range(n)]
        for i, j in queens:
            board[i][j] = 'Q'
        return [''.join(row) for row in board]


class Solution2(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        self.solve(0, n, solutions, [])
        return self.draw(n, solutions)

    def solve(self, k, n, solutions, queens):
        if k == n:
            solutions.append(queens[:])
            return

        for pos in xrange(n):
            if self.valid_move(k, pos, queens):
                self.solve(k + 1, n, solutions, queens + [(k, pos)])

    def valid_move(self, i, j, queens):
        for mi, mj in queens:
            if mj == j:
                return False
            if abs(mi - i) == abs(mj - j):
                return False
        return True

    def draw(self, n, solutions):
        ret = []
        for queens in solutions:
            board = [['.'] * n for _ in range(n)]
            for i, j in queens:
                board[i][j] = 'Q'
                board[i] = ''.join(board[i])
            ret.append(board)
        return ret

