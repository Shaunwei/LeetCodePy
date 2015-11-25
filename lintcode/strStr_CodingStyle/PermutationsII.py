__author__ = 'shawei'
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        if not nums:
            return []

        ret = []
        self.helper(sorted(nums), ret, [])
        return ret

    def helper(self, nums, ret, tmp):
        if not nums:
            ret.append(tmp[:])
            return

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            self.helper(nums[:i] + nums[i + 1:], ret, tmp + [num])
