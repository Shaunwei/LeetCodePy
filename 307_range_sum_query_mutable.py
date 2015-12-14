class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.st = SegmentTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if self.has_tree():
            self.st.update(self.st.root, i, val)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.has_tree():
            return self.st.query(self.st.root, i, j)

    def has_tree(self):
        return self.st is not None

class Node:
    def __init__(self, start, end, sum):
        self.start, self.end = start, end
        self.left = self.right = None
        self.sum = sum


class SegmentTree(object):
    def __init__(self, nums):
        if nums:
            self.root = self.build(nums, 0, len(nums) - 1)
        else:
            self.root = None

    def build(self, nums, l, r):
        if l == r:
            return Node(l, l, nums[l])

        mid = (l + r) / 2
        root = Node(l, r, 0)
        root.left = self.build(nums, l, mid)
        root.right = self.build(nums, mid + 1, r)
        root.sum = root.left.sum + root.right.sum
        return root

    def query(self, root, st, ed):
        if root.start == st and root.end == ed:
            return root.sum

        mid = (root.start + root.end) / 2
        lsum = rsum = 0
        if st <= mid:
            lsum = self.query(root.left, st, min(ed, mid))
        if mid + 1 <= ed:
            rsum = self.query(root.right, max(st, mid + 1), ed)
        return lsum + rsum

    def update(self, root, index, value):
        if root.start == root.end == index:
            root.sum = value
            return

        mid = (root.start + root.end) / 2
        if root.start <= index <= mid:
            self.update(root.left, index, value)
        elif mid + 1 <= index <= root.end:
            self.update(root.right, index, value)
        root.sum = root.left.sum + root.right.sum


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
