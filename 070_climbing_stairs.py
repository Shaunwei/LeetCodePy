class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = r = 1
        for _ in xrange(n - 1):
            l, r = r, l + r
        return r


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 2:
            return n

        far, close = 1, 2
        for _ in xrange(n - 2):
            far, close = close, far + close
        return close
