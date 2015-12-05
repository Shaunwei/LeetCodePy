class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        n = len(height)
        lbars = [0] * n
        hbar = 0
        for i in xrange(n):
            lbars[i] = hbar
            hbar = max(hbar, height[i])

        rbars = [0] * n
        hbar = 0
        for j in reversed(xrange(n)):
            rbars[j] = hbar
            hbar = max(hbar, height[j])

        water = 0
        for k in xrange(1, n - 1):
            mwater = min(lbars[k], rbars[k]) - height[k]
            if mwater > 0:
                water += mwater

        return water


class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        n = len(height)
        lh = [0] * n
        lh[0] = height[0]
        for i in range(1, len(height)):
            lh[i] = max(lh[i - 1], height[i])

        rh = [0] * n
        rh[-1] = height[-1]
        for j in reversed(range(len(height) - 1)):
            rh[j] = max(rh[j + 1], height[j])


        ret = 0
        for i in xrange(1, len(height) - 1):
            ret += min(lh[i], rh[i]) - height[i]
        return ret