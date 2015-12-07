class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # subset
        if n <= 0 or k <= 0 or k > n:
            return []

        ret = []
        self.comb(range(1, n + 1), k, ret, [])
        return ret

    def comb(self, nums, k, ret, tmp):
        if k == 0:
            ret.append(tmp[:])
            return

        for i, num in enumerate(nums):
            self.comb(nums[i + 1:], k - 1, ret, tmp + [num])

