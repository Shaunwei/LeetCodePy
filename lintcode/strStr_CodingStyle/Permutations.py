__author__ = 'shawei'
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # iterative
    # use next permutation
    def permute(self, nums):
        if not nums:
            return []
        res = []
        nums.sort()
        while True:
            res.append(nums[:])
            for i in xrange(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    break
            else:
                return res

            for j in xrange(len(nums) - 1, -1, -1):
                if nums[i] < nums[j]:
                    break

            nums[i], nums[j] = nums[j], nums[i]

            l, r = i + 1, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return res

class Solution2:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # recursive
    def permute(self, nums):
        if not nums:
            return []
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, tmp):
        if not nums:
            res.append(tmp[:])
            return

        for i, num in enumerate(nums):
            self.helper(nums[:i] + nums[i + 1:], res, tmp + [num])

