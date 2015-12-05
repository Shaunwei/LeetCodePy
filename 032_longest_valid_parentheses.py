class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        stack = []
        for i, p in enumerate(s):
            if not stack or p == '(' or stack[-1][0] == ')':
                stack.append((p, i))
            else:
                stack.pop()
                if stack:
                    mlen = i - stack[-1][1]
                else:
                    mlen = i + 1
                longest = max(longest, mlen)
        return longest


class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        longest = 0
        for i, p in enumerate(s):
            if p == '(':
                stack.append((i, p))
            elif p == ')':
                if not stack or stack[-1][1] != '(':
                    stack.append((i, p))
                else:
                    stack.pop()
                    if stack:
                        longest = max(longest, i - stack[-1][0])
                    else:
                        longest = max(longest, i + 1)
        return longest
