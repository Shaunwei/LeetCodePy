class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        4: 45 - 4: 54
        """
        # greedy algorithm
        # almost dp, because we can move two bars
        # but the strategy is, move the lower bar to closer [can be proved]
        if not height:
            return 0

        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(area, max_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area

class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 1:
            return 0

        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                left += 1
            else:
                area = (right - left) * height[right]
                right -= 1
            max_area = max(area, max_area)
        return max_area
