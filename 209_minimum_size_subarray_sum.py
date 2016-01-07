class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        length = len(nums) + 1
        left = 0
        for right in xrange(len(nums)):
            sums += nums[right]
            while sums >= s and left <= right:
                length = min(length, right - left + 1)
                sums -= nums[left]
                left += 1
        if length == len(nums) + 1:
            return 0
        return length
