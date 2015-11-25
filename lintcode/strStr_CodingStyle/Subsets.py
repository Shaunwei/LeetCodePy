__author__ = 'shawei'
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # iterative
        if not S:
            return []

        res = []
        S.sort()
        n = len(S)
        for i in xrange(2 ** n):
            tmp = []
            for j in xrange(n):
                if i & (1 << j) != 0:
                    tmp.append(S[j])
            res.append(tmp)
        # for i in xrange(2**n):
        #     res.append([S[j] for j in xrange(n) if i & (1 << j) != 0])
        return res


class Solution2:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # recursive
        # pythonic
        if not S:
            return []

        res = []
        self.helper(sorted(S), res, [])
        return res

    def helper(self, nums, res, tmp):
        res.append(tmp[:])
        for i, num in enumerate(nums, 1):
            self.helper(nums[i:], res, tmp + [num])


class Solution3:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # recursive
        # more efficient but reduce readability
        if not S:
            return []

        res = []
        self.helper(sorted(S), res, [], 0)
        return res

    def helper(self, nums, res, tmp, pos):
        res.append(tmp[:])
        for i in xrange(pos, len(nums)):
            tmp.append(nums[i])
            self.helper(nums, res, tmp, i + 1)
            tmp.pop()
