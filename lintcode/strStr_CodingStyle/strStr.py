class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        for i in xrange(len(source) - len(target) + 1):
            for j in xrange(len(target)):
                if source[i + j] != target[j]:
                    break
            else:
                return i
        return -1
