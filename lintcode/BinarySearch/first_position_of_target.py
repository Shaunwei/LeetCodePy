class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1

        st, ed = 0, len(nums) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if nums[mid] == target:
                ed = mid
            elif nums[mid] < target:
                st = mid
            else:
                ed = mid
        if nums[st] == target:
            return st
        elif nums[ed] == target:
            return ed
        return -1

