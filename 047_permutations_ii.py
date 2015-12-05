class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.perm(sorted(nums), ret, [])
        return ret

    def perm(self, nums, ret, tmp):
        if not nums:
            ret.append(tmp[:])
            return

        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.perm(nums[:i] + nums[i + 1:], ret, tmp + [nums[i]])
