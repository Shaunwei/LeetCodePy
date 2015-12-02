class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.isValidRow(board, i):
                return False
            if not self.isValidCol(board, i):
                return False

        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                if not self.isValidGrid(board, i, j):
                    return False
        return True

    def isValidRow(self, board, i):
        exist = set()
        for num in board[i]:
            if num != '.' and num in exist:
                return False
            exist.add(num)
        return True

    def isValidCol(self, board, j):
        exist = set()
        for i in range(9):
            num = board[i][j]
            if num != '.' and num in exist:
                return False
            exist.add(num)
        return True

    def isValidGrid(self, board, i, j):
        exist = set()
        for m_i in range(3):
            for m_j in range(3):
                num = board[i + m_i][j + m_j]
                if num != '.' and num in exist:
                    return False
                exist.add(num)
        return True


class Solution2:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        for i, row in enumerate(board):
            # test row
            if not self.isValidRow(row):
                return False

            repeat = set()
            for j in xrange(len(row)):
                if i % 3 == 0 and j % 3 == 0:
                    # test grid
                    if not self.isValidGrid(board, i, j):
                        return False

                # use j as row
                # board[j][i] will check col i
                if board[j][i] == '.':
                    continue
                if board[j][i] in repeat:
                    return False
                else:
                    repeat.add(board[j][i])
        return True

    def isValidRow(self, row):
        repeat = set()
        for val in row:
            if val == '.':
                continue
            if val in repeat:
                return False
            else:
                repeat.add(val)
        return True

    def isValidGrid(self, board, x, y):
        repeat = set()
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if board[i][j] == '.':
                    continue
                if board[i][j] in repeat:
                    return False
                else:
                    repeat.add(board[i][j])
        return True

