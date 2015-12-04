class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        3: 48 - 3:56
        """
        table = dict(zip(list('IVXLCDM'), [1, 5, 10, 50, 100, 500, 1000]))

        # lookup table
        # sequence ordering!
        val = 0
        for i, r in enumerate(s):
            val += table[r]
            if i > 0 and table[s[i - 1]] < table[r]:
                val -= 2 * table[s[i - 1]]
        return val

class Solution2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ret = 0
        for i in xrange(len(s)):
            ret += r2i[s[i]]
            if i > 0 and r2i[s[i]] > r2i[s[i - 1]]:
                ret -= 2 * r2i[s[i - 1]]
        return ret