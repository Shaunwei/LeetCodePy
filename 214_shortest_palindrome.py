class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        for i in xrange((len(s) - 1) / 2, -1, -1):
            if i > 0:
                p = self.form_palindrome(s, i, i - 1)
                if p:
                    return p
            p = self.form_palindrome(s, i, i)
            if p:
                return p

    def form_palindrome(self, s, i, j):
        while i >= 0:
            if s[i] != s[j]:
                return
            i -= 1
            j += 1

        palindrome = s
        for k in xrange(j, len(s)):
            palindrome = s[k] + palindrome
        return palindrome
