class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1

        st, ed = 0, x
        while st + 1 < ed:
            mid = (st + ed) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                st = mid
            else:
                ed = mid
        if ed * ed <= x:
            return ed
        else:
            return st


class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0

        guess, root = 1.0, 0.0
        while guess != root:
            root, guess = guess, (x / guess + guess) / 2
        return int(root)
