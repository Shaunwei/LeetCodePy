class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # sliding window
        l = 0
        max_sum = - 2 ** 31
        cur_sum = 0
        for r in xrange(len(nums)):
            cur_sum += nums[r]
            while l < r and (cur_sum <= nums[r] or nums[l] <= 0):
                cur_sum -= nums[l]
                l += 1
            max_sum = max(max_sum, cur_sum)
        return max_sum


class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # prefix sum
        max_sum = - 2**31
        low_sum = cur_sum = 0
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum - low_sum)
            low_sum = min(cur_sum, low_sum)
        return max_sum

