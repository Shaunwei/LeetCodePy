class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Random order
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     while nums[l] == val and l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         r -= 1
        #     if nums[l] != val:
        #         l += 1
        # return l if nums[l] == val else l + 1


        # keep order
        # l = r = 0
        # while r < len(nums):
        #     if nums[r] != val:
        #         nums[l] = nums[r]
        #         l += 1
        #     r += 1
        # return l
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left


class Solution2:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums:
            return 0

        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] != val:
                l += 1
            while l < r and nums[r] == val:
                r -= 1

            # swap only it exists!!
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if nums[r] == val:
            return r
        else:
            return r + 1