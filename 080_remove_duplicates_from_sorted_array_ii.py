class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts = 2
        if len(nums) <= cnts:
            return len(nums)

        left = 0
        cur_cnt = 1
        for right in xrange(1, len(nums)):
            if nums[right] == nums[left]:
                if cur_cnt < cnts:
                    left += 1
                    nums[left] = nums[right]
                    cur_cnt += 1
            else:
                left += 1
                nums[left] = nums[right]
                cur_cnt = 1
        return left + 1
