class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        6:00 - 6:03
        """
        if not matrix or not matrix[0]:
            return

        zeros = {'row': set(), 'col': set()}
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros['row'].add(i)
                    zeros['col'].add(j)

        for i in xrange(m):
            for j in range(n):
                if i in zeros['row'] or j in zeros['col']:
                    matrix[i][j] = 0

