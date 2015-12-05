class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        max_jump = 0
        for i, jump in enumerate(nums):
            if i > max_jump:
                return False
            else:
                max_jump = max(max_jump, i + jump)
                if max_jump >= len(nums) - 1:
                    return True

class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxjump = 0
        for i, jump in enumerate(nums):
            if maxjump >= i:
                maxjump = max(maxjump, i + jump)
                if maxjump >= len(nums) - 1:
                    return True
        return False
