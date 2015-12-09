"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import collections

ReturnType = collections.namedtuple('ReturnType', ['min', 'max', 'is_bst'])

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # divide conquer
        return self.is_valid_bst(root).is_bst

    def is_valid_bst(self, root):
        if not root:
            return ReturnType(10**10, -10**10, True)

        left = self.is_valid_bst(root.left)
        right = self.is_valid_bst(root.right)

        if left.is_bst and right.is_bst and left.max < root.val < right.min:
            return ReturnType(
                    min(left.min, root.val),
                    max(right.max, root.val),
                    True)
        else:
            return ReturnType(0, 0, False)


class Solution2:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        prev = None
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                curt = stack.pop()
                if prev and prev.val >= curt.val:
                    return False
                prev = curt
                root = curt.right
        return True
