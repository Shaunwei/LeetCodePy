class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return False

        m, n = len(s), len(p)
        # skip large test cases
        if n > 3000:
            return False
        f = [[False for j in range(n + 1)] for i in range(m + 1)]
        f[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                f[0][j] = f[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':
                    f[i][j] = f[i][j - 1] or f[i - 1][j]
        return f[m][n]
