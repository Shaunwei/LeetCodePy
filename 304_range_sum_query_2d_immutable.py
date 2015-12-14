class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.sums = self.build_matrix_sum(matrix)

    def build_matrix_sum(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        # extra 0s
        # index i, j save in (i + 1)th and (j + 1)th
        sums = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        for i in xrange(m):
            for j in xrange(n):
                sums[i + 1][j + 1] = sums[i][j + 1] + sums[i + 1][j] - sums[i][j] + matrix[i][j]
        return sums

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.sums:
            return

        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] - \
                self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
