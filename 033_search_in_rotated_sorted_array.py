class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        st, ed = 0, len(nums) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if nums[mid] == target:
                return mid
            elif nums[st] < nums[mid]:
                if nums[st] <= target < nums[mid]:
                    ed = mid
                else:
                    st = mid
            elif nums[mid] < nums[ed]:
                if nums[mid] < target <= nums[ed]:
                    st = mid
                else:
                    ed = mid

        if nums[st] == target:
            return st
        elif nums[ed] == target:
            return ed
        else:
            return -1
