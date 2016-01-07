class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        repeat = set()
        while n != 1 and n not in repeat:
            repeat.add(n)
            temp = 0
            while n:
                temp += (n % 10) ** 2
                n /= 10
            n = temp
        return n == 1
