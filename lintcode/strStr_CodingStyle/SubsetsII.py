__author__ = 'shawei'
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        if not S:
            return []

        res = []
        self.helper(sorted(S), res, [])
        return res

    def helper(self, nums, res, tmp):
        res.append(tmp[:])
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            self.helper(nums[i + 1:], res, tmp + [num])
