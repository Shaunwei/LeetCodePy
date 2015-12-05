class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        st, ed = 0, m * n - 1

        while st + 1 < ed:
            mid = (st + ed) / 2
            mid_val = matrix[mid / n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                st = mid
            else:
                ed = mid

        return matrix[st / n][st % n] == target or \
                matrix[ed / n][ed % n] == target

