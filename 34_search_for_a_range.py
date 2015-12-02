class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [-1, -1]
        if not nums:
            return ret

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
            ret[0] = st
        elif nums[ed] == target:
            ret[0] = ed

        st, ed = 0, len(nums) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if nums[mid] == target:
                st = mid
            elif nums[mid] < target:
                st = mid
            else:
                ed = mid
        if nums[ed] == target:
            ret[1] = ed
        elif nums[st] == target:
            ret[1] = st
        return ret
