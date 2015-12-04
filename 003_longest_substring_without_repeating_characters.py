__author__ = 'shawei'
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        4: 29 - 4: 37
        """
        # sliding window
        # no repeat, update left bound strategy [repeat and >= left]
        max_len = 0
        left = 0
        repeat = {}
        for right, char in enumerate(s):
            if char in repeat and repeat[char] >= left:
                left = repeat[char] + 1
            repeat[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

