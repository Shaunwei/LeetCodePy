"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # divide conquer
        if not root:
            return 0

        lmd = self.maxDepth(root.left)
        rmd = self.maxDepth(root.right)
        return max(lmd, rmd) + 1


class Solution2:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # traversal way
        self.max_depth = 0
        self.dfs(root, 0)
        return self.max_depth

    def dfs(self, root, depth):
        if root:
            depth += 1
            self.dfs(root.left, depth)
            self.max_depth = max(self.max_depth, depth)
            self.dfs(root.right, depth)