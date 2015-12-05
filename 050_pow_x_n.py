class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        elif n > 0:
            return self.pow(x, n)
        else:
            return 1 / self.pow(x, -n)

    def pow(self, x, n):
        if n == 1:
            return x

        if n % 2 == 0:
            return self.pow(x * x, n / 2)
        else:
            return x * self.pow(x * x, (n - 1) / 2)


class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return self.pow(x, n) if n >= 0 else 1 / self.pow(x, -n)

    def pow(self, x, n):
        if n == 0:
            return 1

        if n % 2 == 0:
            return self.pow(x * x, n / 2)
        else:
            return x * self.pow(x * x, n / 2)
