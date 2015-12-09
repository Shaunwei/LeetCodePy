"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.root = root

    #@return: True if there has next node, or false
    def hasNext(self):
        return len(self.stack) > 0 or self.root is not None

    #@return: return next node
    def next(self):
        if self.hasNext():
            while self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            node = self.stack.pop()
            self.root = node.right
            return node
