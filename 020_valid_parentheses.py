class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack problem
        # careful when function end, stack content!!!
        table = dict(zip('([{', ')]}'))

        stack = []
        for p in s:
            if p in '([{':
                stack.append(p)
            elif p in ')]}':
                if not stack or table[stack.pop()] != p:
                    return False
            else:
                return False
        return len(stack) == 0

class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = dict(zip('([{', ')]}'))

        for char in s:
            if char in table:
                stack.append(table[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        if stack:
            return False
        return True