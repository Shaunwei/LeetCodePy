class Trie:
    class TrieNode:
        def __init__(self, char=''):
            self.char = char
            self.word = False
            self.children = {}

    def __init__(self):
        self.root = Trie.TrieNode()

    def add(self, word):
        if not word:
            return
        root = self.root
        for i, char in enumerate(word):
            if char not in root.children:
                root.children[char] = Trie.TrieNode(char)
            root = root.children[char]
        root.word = True

    def search(self, word):
        if not word:
            return True
        return self.search_rec(self.root, word)

    def search_rec(self, root, word):
        if not word:
            return root.word
        elif word[0] in root.children:
            root = root.children[word[0]]
            return self.search_rec(root, word[1:])
        elif word[0] == '.':
            for _, node in root.children.iteritems():
                if self.search_rec(node, word[1:]):
                    return True
        return False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
