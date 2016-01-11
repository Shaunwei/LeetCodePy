import collections

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False

        window = collections.OrderedDict()
        for i, num in enumerate(nums):
            if i > k:
                window.popitem(last=False)

            bucket = num / t if t else num
            for j in window.get(bucket - 1), window.get(bucket), window.get(bucket + 1):
                if j is not None and abs(nums[i] - nums[j]) <= t:
                    return True
            if bucket in window:
                window.pop(bucket)
            window[bucket] = i
        return False
