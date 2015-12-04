__author__ = 'shawei'
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        4: 40 - 4: 45
        """
        # palindrome prepare
        # iterate i,i and i, i+1
        longest = ''
        for i in range(len(s)):
            tmp = self.find(s, i, i)
            if len(tmp) > len(longest):
                longest = tmp
            tmp = self.find(s, i, i + 1)
            if len(tmp) > len(longest):
                longest = tmp
        return longest

    def find(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1: j]
