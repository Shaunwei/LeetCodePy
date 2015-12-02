class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            self.reverse(nums, 0, len(nums) - 1)
            return

        for j in xrange(len(nums) - 1, -1, -1):
            if nums[j] > nums[i]:
                break

        nums[i], nums[j] = nums[j], nums[i]

        self.reverse(nums, i + 1, len(nums) - 1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


class Solution2:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if not nums or len(nums) == 1:
            return

        # 1
        # first val that is not increasing
        for i in reversed(xrange(len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                break

        # Exception!
        # all increasing
        if i == 0 and nums[i] > nums[i + 1]:
            self.reverse(nums, 0, len(nums) - 1)
            return

        # 2
        # first val that is larger than nums[i]
        for j in reversed(xrange(len(nums))):
            if nums[j] > nums[i]:
                break

        # 3
        # swap i, j
        nums[i], nums[j] = nums[j], nums[i]

        # 4
        # reverse
        self.reverse(nums, i + 1, len(nums) - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

