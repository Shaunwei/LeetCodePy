class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        6:17 - 6:22
        """
        # tricky return what, be careful to compare
        if not nums or len(nums) < 3:
            return

        ret = 2 ** 31 - 1
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(s - target) < abs(ret - target):
                    ret = s
                if s > target:
                    k -= 1
                else:
                    j += 1
        return ret

class Solution2(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return

        ret = 0
        diff = 2**31 - 1
        nums.sort()

        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if diff > abs(s - target):
                    diff = abs(s - target)
                    ret = s

                if s == target:
                    return target
                elif s > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return ret
