class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        11:34 -
        """
        words = s.split()
        if not words:
            return 0
        else:
            return len(words[-1])

class Solution2(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not s.rstrip():
            return 0
        return len(s.split()[-1])