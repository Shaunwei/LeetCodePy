__author__ = 'shawei'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 3:22 - 3:28
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31


        is_pos = x >= 0
        rint = int(str(abs(x))[::-1])
        rint = rint if is_pos else rint * -1

        if rint > MAX_INT or rint < MIN_INT:
            return 0
        else:
            return rint

class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1

        val = int(''.join(str(abs(x))[::-1]))
        if val < -2**31 or val > 2**31 - 1:
            return 0
        return sign * val