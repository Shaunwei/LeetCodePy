class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])

        top, down = 0, m - 1
        left, right = 0, n - 1
        ret = []
        directions = 0
        while top <= down and left <= right:
            if directions % 4 == 0:
                for j in range(left, right + 1):
                    ret.append(matrix[top][j])
                top += 1
            elif directions % 4 == 1:
                for i in range(top, down + 1):
                    ret.append(matrix[i][right])
                right -= 1
            elif directions % 4 == 2:
                for j in reversed(range(left, right + 1)):
                    ret.append(matrix[down][j])
                down -= 1
            elif directions % 4 == 3:
                for i in reversed(range(top, down + 1)):
                    ret.append(matrix[i][left])
                left += 1
            directions += 1
        return ret


class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        ret = []
        m, n = len(matrix), len(matrix[0])
        mleft, mright = 0, n - 1
        mtop, mdown = 0, m - 1
        while True:
            for j in range(mleft, mright + 1):
                ret.append(matrix[mtop][j])
            mtop += 1
            if mtop > mdown:
                break
            for i in range(mtop, mdown + 1):
                ret.append(matrix[i][mright])
            mright -= 1
            if mleft > mright:
                break
            for j in reversed(range(mleft, mright + 1)):
                ret.append(matrix[mdown][j])
            mdown -= 1
            if mtop > mdown:
                break
            for i in reversed(range(mtop, mdown + 1)):
                ret.append(matrix[i][mleft])
            mleft += 1
            if mleft > mright:
                break
        return ret
