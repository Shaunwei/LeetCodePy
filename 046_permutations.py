class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.perm(nums, ret, [])
        return ret

    def perm(self, nums, ret, tmp):
        if not nums:
            ret.append(tmp[:])
            return

        for i in xrange(len(nums)):
            self.perm(nums[:i] + nums[i + 1:], ret, tmp + [nums[i]])
