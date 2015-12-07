class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0 for j in range(n)] for i in range(m)]
        f[0][0] = 1
        for i in range(1, m):
            f[i][0] = f[i - 1][0] if not obstacleGrid[i][0] else 0
        for j in range(1, n):
            f[0][j] = f[0][j - 1] if not obstacleGrid[0][j] else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]
