"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        if not root:
            return 0

        return self.max_path_sum(root)[0]

    def max_path_sum(self, root):
        if not root:
            return -2**31, 0

        lmps, lp = self.max_path_sum(root.left)
        rmps, rp = self.max_path_sum(root.right)

        curp = max(lp, rp, 0) + root.val
        mps = max(lmps, rmps, curp, lp + rp + root.val)

        return mps, curp

class Solution2:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):

        return self.max_path_sum(root)[1]

    def max_path_sum(self, root):
        if not root:
            return 0, -10**10

        left_single_path, left_max_path = self.max_path_sum(root.left)
        right_single_path, right_max_path = self.max_path_sum(root.right)

        single_path = max(left_single_path, right_single_path) + root.val
        single_path = max(single_path, 0)

        max_path = max(left_max_path, right_max_path)
        max_path = max(max_path, left_single_path+right_single_path+root.val)

        return single_path, max_path
