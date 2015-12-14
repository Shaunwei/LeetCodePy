class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = self.build_sum_array(nums)

    def build_sum_array(self, nums):
        if not nums:
            return []

        sums = [0] * len(nums)
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            sums[i] = cur
        return sums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i - 1]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
