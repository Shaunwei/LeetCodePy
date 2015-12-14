class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        for k in xrange(m + n - 1, -1, -1):
            v1 = nums1[i] if i >= 0 else -10**10
            v2 = nums2[j] if j >= 0 else -10**10
            if v1 > v2:
                nums1[k] = v1
                i -= 1
            else:
                nums1[k] = v2
                j -= 1
