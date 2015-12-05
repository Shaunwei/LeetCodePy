class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left = right = 0
        jumps = 0

        while left <= right and right < len(nums) - 1:
            jumps += 1
            max_jump = right
            for i in range(left, right + 1):
                max_jump = max(max_jump, nums[i] + i)
            left, right = right + 1, max_jump

        if right >= len(nums) - 1:
            return jumps
        else:
            return 0


class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        start, end = 0, 0
        jumps = 0
        while end < len(nums) - 1:
            jumps += 1
            max_jump = end
            for i in range(start, end + 1):
                max_jump = max(max_jump, nums[i] + i)
            start = end + 1
            end = max_jump
        return jumps