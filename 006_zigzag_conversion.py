__author__ = 'shawei'
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # simple repeat
        # two conditions in while
        if not numRows or not s:
            return ''

        rows = [[] for _ in range(numRows)]

        i = 0
        while i < len(s):
            n = 0
            while i < len(s) and n < numRows:
                rows[n].append(s[i])
                n += 1
                i += 1
            n -= 2
            while i < len(s) and n > 0:
                rows[n - numRows].append(s[i])
                n -= 1
                i += 1

        return ''.join(''.join(row) for row in rows)

import itertools
class Solution2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for _ in range(numRows)]

        i = 0
        try:
            while True:
                for j in range(numRows):
                    rows[j].append(s[i])
                    i += 1
                for k in reversed(range(1, numRows - 1)):
                    rows[k].append(s[i])
                    i += 1
        except IndexError:
            return ''.join(itertools.chain(*rows))