class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    # @param root, start, end: The root of segment tree and
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        if not root:
            return -2**31

        if root.start == start and root.end == end:
            return root.max

        mid = (root.start + root.end) / 2
        left = right = -2**31
        if start <= mid:
            left = self.query(root.left, max(start, root.start), min(mid, end))
        if mid + 1 <= end:
            right = self.query(root.right, max(mid + 1, start), min(end, root.end))
        return max(left, right)


class Solution:
    # @param root, start, end: The root of segment tree and
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.max

        mid = (root.start + root.end) / 2
        leftmax = rightmax = -2**31

        # left subtree
        if start <= mid:
            if mid < end:  # fen lie
                leftmax = self.query(root.left, start, mid)
            else:  # xiang jiao
                leftmax = self.query(root.left, start, end)
            # leftmax = self.query(root.left, start, min(end, mid))

        # right subtree
        if mid < end:
            if start <= mid:  # fen lie
                rightmax = self.query(root.right, mid + 1, end)
            else:
                rightmax = self.query(root.right, start, end)
            # rightmax = self.query(root.right, max(start, mid + 1), end)

        root.max = max(leftmax, rightmax)
        return root.max
