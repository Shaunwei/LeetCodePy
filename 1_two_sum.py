__author__ = 'shawei'

import collections
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        4:09 - 4:18
        """
        # for i in xrange(len(nums) - 1):
        #     for j in xrange(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i + 1, j + 1]
        # return [-1, -1]

        # dict
        # duplicate nums with additional indexes
        vals = collections.defaultdict(list)
        for i, num in enumerate(nums):
            vals[num].append(i + 1)

        for val in vals:
            if target - val in vals:
                if target - val == val:
                    if len(vals[val]) >= 2:
                        return vals[val][:2]
                else:
                    return sorted([vals[val][0], vals[target - val][0]])
        return []

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {num: i for i, num in enumerate(nums, 1)}

        for i, num in enumerate(nums, start=1):
            if target - num in num_dict:
                j = num_dict[target - num]
                if i < j:
                    return [i, j]
        return [-1, -1]