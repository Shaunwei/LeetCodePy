# online algorithm
# this is recommanded
class Solution0(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words:
            return []

        ret = []
        for word in words:
            if self.find_word(board, word):
                ret.append(word)
        return ret

    def find_word(self, board, word):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs_has_word(board, word, i, j, set()):
                    return True
        return False

    def dfs_has_word(self, board, word, i, j, marked):
        if not word:
            return True
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return False

        if (i, j) in marked:
            return False
        if word[0] != board[i][j]:
            return False

        marked.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            if self.dfs_has_word(board, word[1:], i + dx, j + dy, marked):
                return True
        marked.remove((i, j))
        return False


# OJ solution
class Trie:
    class TrieNode:
        def __init__(self, char=''):
            self.char = char
            self.word = ''
            self.children = {}

    def __init__(self):
        self.root = Trie.TrieNode()

    def add(self, word):
        if not word:
            return
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = Trie.TrieNode(char)
            root = root.children[char]
        root.word = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.add(word)

        ret = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs_find_word(board, i, j, trie.root, set(), ret)
        return list(ret)

    def dfs_find_word(self, board, i, j, root, marked, ret):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return
        if (i, j) in marked:
            return
        marked.add((i, j))

        if board[i][j] in root.children:
            root = root.children[board[i][j]]
            if root.word:
                ret.add(root.word)
            for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                self.dfs_find_word(board, i + di, j + dj, root, marked, ret)
        marked.remove((i, j))
