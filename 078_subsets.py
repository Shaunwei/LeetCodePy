class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.helper(sorted(nums), 0, ret, [])
        return ret

    def helper(self, nums, st, ret, tmp):
        ret.append(tmp[:])

        for i in xrange(st, len(nums)):
            tmp.append(nums[i])
            self.helper(nums, i + 1, ret, tmp)
            tmp.pop()


class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        self.subset(nums, ret, [])
        return ret

    def subset(self, nums, ret, tmp):
        ret.append(tmp[:])
        for i, n in enumerate(nums):
            self.subset(nums[i + 1:], ret, tmp + [n])
