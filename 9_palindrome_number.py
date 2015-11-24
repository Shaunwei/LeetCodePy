__author__ = 'shawei'
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        3: 42 - 3: 47
        """
        # reverse last digit
        # careful about 0, 10, 1000... bacause last bit will be 0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        y = x % 10
        x /= 10
        while x > y:
            val = x % 10
            x /= 10
            y = y * 10 + val

        return x == y or x == y / 10

class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        st, ed = 0, len(a) - 1
        while st < ed:
            if a[st] != a[ed]:
                return False
            st += 1
            ed -= 1
        return True