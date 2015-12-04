class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4:
            return []

        ret = set()
        nums.sort()
        sums = collections.defaultdict(list)
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                sums[nums[i] + nums[j]].append([i, j])

        for i in xrange(len(nums) - 3):
            for j in xrange(i + 1, len(nums) - 2):
                if target - nums[i] - nums[j] in sums:
                    slist = sums[target - nums[i] - nums[j]]
                    for m, n in slist:
                        if j < m:
                            ret.add((nums[i], nums[j], nums[m], nums[n]))
        return [list(r) for r in ret]
