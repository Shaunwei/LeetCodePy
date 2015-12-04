class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        st, ed = 0, len(nums) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if nums[mid] == target:
                ed = mid
            elif nums[mid] < target:
                st = mid
            else:
                ed = mid
        if nums[st] >= target:
            return st
        elif nums[ed] >= target:
            return ed
        return len(nums)
