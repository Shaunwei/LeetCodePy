__author__ = 'shawei'
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        5: 16 - 5:44
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.findkth(nums1, nums2, length / 2) +
                    self.findkth(nums1, nums2, length / 2 + 1)) / 2.0
        else:
            return self.findkth(nums1, nums2, length / 2 + 1)

    def findkth(self, A, B, k):
        if len(B) > len(A):
            return self.findkth(B, A, k)
        if not B:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        if len(B) >= k / 2 and B[k / 2 - 1] < A[k / 2 - 1]:
            return self.findkth(A, B[k / 2:], k - k / 2)
        else:
            return self.findkth(A[k / 2:], B, k - k / 2)

