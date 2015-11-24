class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        3:58 - 4:02
        """
        # reduce function `compare each two`
        # map-reduce
        if not strs:
            return ''
        return reduce(self.prefix, strs)

    def prefix(self, a, b):
        i = 0
        while i < min(len(a), len(b)):
            if a[i] == b[i]:
                i += 1
            else:
                break
        return a[:i]

class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        def prefix(a, b):
            i = 0
            while i < min(len(a), len(b)):
                if a[i] == b[i]:
                    i += 1
                else:
                    break
            return a[:i]

        return reduce(prefix, strs)