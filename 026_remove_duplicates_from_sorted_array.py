class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        l = 0
        for r in xrange(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1


class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        # if len(nums) == 1:
        #     return 1

        # write = 0
        # for read, val in enumerate(nums):
        #     if not read or val == nums[write]:
        #         continue
        #     write += 1
        #     nums[write] = val
        # return write + 1

        slow = 0
        for fast in xrange(1, len(nums)):
            if nums[fast] == nums[slow]:
                continue
            slow += 1
            nums[slow] = nums[fast]
        return slow + 1