class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = 0
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        f = [[0 for j in xrange(n)] for i in xrange(m)]
        for j in xrange(n):
            if matrix[0][j] == '1':
                max_area = 1
                f[0][j] = 1
        for i in xrange(m):
            if matrix[i][0] == '1':
                max_area = 1
                f[i][0] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    f[i][j] = 1 + min(f[i-1][j-1], f[i-1][j], f[i][j-1])
                    max_area = max(max_area, f[i][j] ** 2)
        return max_area

if __name__ == '__main__':
    matrix = [
      '0010',
      '0011',
      '1111'
    ]
    print(Solution().maximalSquare(matrix))
