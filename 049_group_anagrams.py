import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = collections.defaultdict(list)
        for s in strs:
            group[''.join(sorted(s))].append(s)

        return [sorted(vals) for vals in group.values() if vals]
