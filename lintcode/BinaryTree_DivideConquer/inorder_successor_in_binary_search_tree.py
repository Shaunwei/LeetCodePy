# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # path solution
        path = []
        while root and root.val != p.val:
            path.append(root)
            if root.val < p.val:
                root = root.right
            else:
                root = root.left

        if not root:
            return

        if root.right:
            root = root.right
            while root.left:
                root = root.left
            return root

        while path:
            parent = path.pop()
            if parent.left is root:
                return parent
            else:
                root = parent
        return


class Solution2(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        successor = None
        while root and root.val != p.val:
            if root.val < p.val:
                root = root.right
            else:
                successor = root
                root = root.left

        if not root:
            return

        if not root.right:
            return successor

        root = root.right
        while root.left:
            root = root.left
        return root