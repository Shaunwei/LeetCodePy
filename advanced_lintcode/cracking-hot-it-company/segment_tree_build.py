class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None


class Solution:
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(start, end)
        if start != end:
            mid = (start + end) / 2
            root.left = self.build(start, mid)
            root.right = self.build(mid + 1, end)
        return root


class Solution:
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        '''
        http://www.jiuzhang.com/solutions/segment-tree-build/
        '''
        if start > end:
            return None

        root = SegmentTreeNode(start, end)

        # rec fen lie
        if start != end:
            mid = (start + end) / 2
            root.left = self.build(start, mid)
            root.right = self.build(mid + 1, end)
            # root.max = max(root.left.max, root.right.max)

        # update
        return root
