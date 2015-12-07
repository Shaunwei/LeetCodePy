class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # counting sort
        if not nums:
            return

        colors = 3
        counts = [0 for _ in range(colors)]
        for num in nums:
            counts[num] += 1

        pos = 0
        for color in range(colors):
            for _ in range(counts[color]):
                nums[pos] = color
                pos += 1


class Solution2(object):
    def sortColors(self, nums):
        # dutch flag
        if not nums:
            return

        pivot = 1
        i, j = 0, len(nums) - 1
        curt = 0
        while curt <= j:
            if nums[curt] == pivot:
                curt += 1
            elif nums[curt] < pivot:
                nums[curt], nums[i] = nums[i], nums[curt]
                curt += 1
                i += 1
            elif nums[curt] > pivot:
                nums[curt], nums[j] = nums[j], nums[curt]
                j -= 1

