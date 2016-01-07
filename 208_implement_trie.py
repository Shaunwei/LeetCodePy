class TrieNode(object):
    def __init__(self, char=''):
        """
        Initialize your data structure here.
        """
        self.char = char
        self.word = False
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        root = self.root
        self.insert_iter(root, word)

    # def insert_rec(self, root, word):
    #     if word[0] not in root.children:
    #         root.children[word[0]] = TrieNode(word[0])

    #     if len(word) == 1:
    #         root.children[word].word = True
    #     else:
    #         self.insert_rec(root.children[word[0]], word[1:])

    def insert_iter(self, root, word):
        for i, char in enumerate(word):
            if char not in root.children:
                root.children[char] = TrieNode(char)

            if i == len(word) - 1:
                root.children[char].word = True
            else:
                root = root.children[char]


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            else:
                root = root.children[char]
        return root.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
