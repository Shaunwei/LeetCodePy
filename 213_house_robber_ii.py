class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)

        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums):
        l = r = 0
        for num in nums:
            l, r = r, max(l + num, r)
        return r
