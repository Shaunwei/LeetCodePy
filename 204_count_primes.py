class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = [True] * n
        cnts = 0
        for p in xrange(2, n):
            if primes[p]:
                cnts += 1
                for i in xrange(2 * p, n, p):
                    primes[i] = False
        return cnts
