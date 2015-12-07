class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[0 for j in range(n)] for i in range(m)]
        f[0][0] = 1
        for i in range(1, m):
            f[i][0] = 1
        for j in range(1, n):
            f[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0

        paths = [[1 for j in range(n)] for i in range(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        return paths[m - 1][n - 1]
