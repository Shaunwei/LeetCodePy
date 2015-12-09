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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # iter
        ret = []
        stack = []
        while stack or root:
            if root:
                ret.append(root.val)
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return ret


class Solution2:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # rec
        ret = []
        self.preorder(root, ret)
        return ret

    def preorder(self, root, ret):
        if root:
            ret.append(root.val)
            self.preorder(root.left, ret)
            self.preorder(root.right, ret)