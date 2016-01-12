"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        if not A:
            return
        return self.build_tree(A, 0, len(A) - 1)

    def build_tree(self, A, st, ed):
        if st == ed:
            return SegmentTreeNode(st, ed, A[st])

        mid = (st + ed) / 2

        root = SegmentTreeNode(st, ed, -1)
        root.left = self.build_tree(A, st, mid)
        root.right = self.build_tree(A, mid + 1, ed)

        root.max = max(root.left.max, root.right.max)
        return root
