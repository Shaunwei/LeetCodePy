class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top, down = 0, n - 1
        left, right = 0, n - 1

        k = 1
        dirc = 0
        while k <= n * n:
            if dirc % 4 == 0:
                for j in range(left, right + 1):
                    matrix[top][j] = k
                    k += 1
                top += 1
            elif dirc % 4 == 1:
                for i in range(top, down + 1):
                    matrix[i][right] = k
                    k += 1
                right -= 1
            elif dirc % 4 == 2:
                for j in reversed(range(left, right + 1)):
                    matrix[down][j] = k
                    k += 1
                down -= 1
            elif dirc % 4 == 3:
                for i in reversed(range(top, down + 1)):
                    matrix[i][left] = k
                    k += 1
                left += 1
            # update directions
            dirc += 1
        return matrix


class Solution2(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        mleft, mright = 0, n - 1
        mtop, mdown = 0, n - 1
        val = 1
        while True:
            for j in range(mleft, mright + 1):
                matrix[mtop][j] = val
                val += 1
            mtop += 1
            if mtop > mdown:
                break

            for i in range(mtop, mdown + 1):
                matrix[i][mright] = val
                val += 1
            mright -= 1
            if mleft > mright:
                break

            for j in reversed(range(mleft, mright + 1)):
                matrix[mdown][j] = val
                val += 1
            mdown -= 1
            if mtop > mdown:
                break

            for i in reversed(range(mtop, mdown + 1)):
                matrix[i][mleft] = val
                val += 1
            mleft += 1
            if mleft > mright:
                break

        return matrix

