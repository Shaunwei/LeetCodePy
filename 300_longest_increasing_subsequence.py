class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        # state: LIS use f[i]
        # init: f[0..n-1] = 1
        # function: f[i] = MAX{f[j] + 1} (j < i, if nums[j] < nums[i])
        # answer: max(f)
        if not nums:
            return 0

        f = [1 for i in range(len(nums))]
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)


class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # patience sort
        # http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
        # “end element of smaller list is smaller than end elements of larger lists”.
        tail_table = [None] * len(nums)
        length = 0
        for num in nums:
            if tail_table[0] is None:
                tail_table[0] = num
                length += 1
            elif tail_table[0] > num:
                tail_table[0] = num
            elif tail_table[length - 1] < num:
                tail_table[length] = num
                length += 1
            else:
                index = self.bs(tail_table, 0, length - 1, num)
                tail_table[index] = num
        return length

    def bs(self, values, l, r, target):
        while l + 1 < r:
            mid = (l + r) / 2
            if values[mid] == target:
                r = mid
            elif values[mid] < target:
                l = mid
            else:
                r = mid
        if values[l] >= target:
            return l
        if values[r] >= target:
            return r
        return -1
