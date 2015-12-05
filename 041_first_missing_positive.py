class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            while nums[i] != i + 1:
                if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[nums[i] - 1]:
                    break
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp

        for j, num in enumerate(nums):
            if num != j + 1:
                return j + 1
        return len(nums) + 1

