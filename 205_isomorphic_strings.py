class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return self.is_isom(s, t) and self.is_isom(t, s)

    def is_isom(self, s, t):
        table = {}
        for i, char in enumerate(s):
            if char not in table:
                table[char] = t[i]
            else:
                if table[char] != t[i]:
                    return False
        return True
