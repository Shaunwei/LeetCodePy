class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    """
    @param root, index, value: The root of segment tree and
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """
    def modify(self, root, index, value):
        if root.start == root.end == index:
            root.max = value
            return

        mid = (root.start + root.end) / 2
        if root.start <= index <= mid:
            self.modify(root.left, index, value)
        elif mid < index <= root.right:
            self.modify(root.right, index, value)
        root.max = max(root.left.max, root.right.max)


class Solution:
    """
    @param root, index, value: The root of segment tree and
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """
    def modify(self, root, index, value):
        if root.start == root.end == index:
            root.max = value
            return

        # query
        mid = (root.start + root.end) / 2
        if root.start <= index <= mid:
            self.modify(root.left, index, value)

        if mid < index <= root.end:
            self.modify(root.right, index, value)

        # update
        root.max = max(root.left.max, root.right.max)
