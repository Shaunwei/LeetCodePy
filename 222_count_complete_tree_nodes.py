# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        lvl = self.get_level(root)
        st, ed = 2 ** lvl, 2 ** (lvl + 1) - 1
        return self.bs(root, st, ed)

    def get_level(self, root):
        lvl = 0
        while root.left:
            lvl += 1
            root = root.left
        return lvl

    def bs(self, root, st, ed):
        while st + 1 < ed:
            mid = (st + ed) / 2
            if self.exist_node(root, mid):
                st = mid
            else:
                ed = mid
        if self.exist_node(root, ed):
            return ed
        else:
            return st

    def exist_node(self, root, val):
        bval = bin(val)[3:]
        for v in bval:
            if v == '0':
                root = root.left
            else:
                root = root.right
        if root is None:
            return False
        else:
            return True
