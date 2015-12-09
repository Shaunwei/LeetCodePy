"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        if not root:
            return

        return self.max_path_sum(root)

    def max_path_sum(self, root):
        if not root:
            return - 2 ** 31

        lmps = self.max_path_sum(root.left)
        rmps = self.max_path_sum(root.right)

        mps = max(lmps, rmps)
        if mps <= 0:
            return root.val
        else:
            return mps + root.val

class Solution2:
    def maxPathSum2(self, root):
        if not root:
            return 0

        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)
        return root.val + max(0, max(left, right))
