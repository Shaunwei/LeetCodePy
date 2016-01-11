import collections

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        duplicates = collections.defaultdict(list)
        for pos, num in enumerate(nums):
            duplicates[num].append(pos)

        for num, positions in duplicates.iteritems():
            if len(positions) > 1:
                for i in xrange(1, len(positions)):
                    if positions[i] - positions[i - 1] <= k:
                        return True
        return False
