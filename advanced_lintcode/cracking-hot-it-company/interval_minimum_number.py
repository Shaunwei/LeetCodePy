"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class SegTree:
    def __init__(self, st, ed, min=-2**31):
        self.st, self.ed = st, ed
        self.min = min

    def query(self, interval):
        root = self
        st, ed = interval.start, interval.end
        return self.query_rec(root, st, ed)

    def query_rec(self, root, st, ed):
        if root.st == st and root.ed == ed:
            return root.min

        mid = (root.st + root.ed) / 2
        left_min = right_min = 2**31 - 1
        if st <= mid:
            left_min = self.query_rec(root.left, max(st, root.st), min(mid, ed))
        if mid < ed:
            right_min = self.query_rec(root.right, max(mid + 1, st), min(root.ed, ed))
        return min(left_min, right_min)

    @staticmethod
    def build(A, st, ed):
        if st == ed:
            return SegTree(st, ed, A[st])
        else:
            mid = (st + ed) / 2
            root = SegTree(st, ed)
            root.left = SegTree.build(A, st, mid)
            root.right = SegTree.build(A, mid + 1, ed)
            root.min = min(root.left.min, root.right.min)
            return root


class Solution:
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        if not A or not queries:
            return []
        segment_tree = SegTree.build(A, 0, len(A) - 1)
        return [segment_tree.query(q) for q in queries]
