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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        return self.is_balanced(root)[0]

    def is_balanced(self, root):
        if not root:
            return True, 0

        left_balanced, left_depth = self.is_balanced(root.left)
        right_balanced, right_depth = self.is_balanced(root.right)

        if left_balanced and right_balanced and abs(left_depth-right_depth) <= 1:
            is_balanced = True
        else:
            is_balanced = False

        return is_balanced, max(left_depth, right_depth) + 1
