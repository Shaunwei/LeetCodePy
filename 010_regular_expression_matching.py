class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        dp
        """
        m, n = len(s), len(p)
        match = [[False for j in range(n + 1)] for i in range(m + 1)]

        match[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                match[0][j] = match[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    match[i][j] = match[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if j == 1:
                        match[i][j] = match[i][j - 1]
                    else:
                        match[i][j] = match[i][j - 1] or match[i][j - 2] or \
                                        (match[i - 1][j] and (p[j - 2] == '.' or p[j - 2] == s[i - 1]))
        return match[m][n]

class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        f = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        f[0][0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                f[0][j] = f[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if j >= 2:
                        f[i][j] = f[i][j - 1] or f[i][j - 2] or \
                                    (f[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                    else:
                        f[i][j] = f[i][j - 1]
        return f[len(s)][len(p)]
