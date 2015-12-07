import re

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = re.split(r'\/+', path)
        stack = []
        for p in paths:
            # could match empty str, before and after
            # need to remove empty match
            if p == '.' or not p:
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)


class Solution2(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # strip at both end
        # no empty match will generate
        paths = re.split(r'/+', path.strip('/'))
        lst = []
        for p in paths:
            if p == '.':
                continue
            elif p == '..':
                if lst:
                    lst.pop()
            else:
                lst.append(p)
        return '/' + '/'.join(lst)
