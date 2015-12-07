class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        # if not word:
        #     return True

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs_has_word(board, i, j, word):
                    return True
        return False

    def dfs_has_word(self, board, i, j, word):
        if not word:
            return True
        # cross boundary
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        # not same char
        if board[i][j] != word[0]:
            return False

        temp = board[i][j]
        board[i][j] = '$$'
        if self.dfs_has_word(board, i + 1, j, word[1:]) or \
            self.dfs_has_word(board, i, j + 1, word[1:]) or \
            self.dfs_has_word(board, i - 1, j, word[1:]) or \
            self.dfs_has_word(board, i, j - 1, word[1:]):
            return True
        board[i][j] = temp
        return False
