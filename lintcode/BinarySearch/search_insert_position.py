class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # first pos that val is >=  target
        if not A:
            return 0

        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if A[mid] == target:
                ed = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid

        if A[st] >= target:
            return st
        elif A[ed] >= target:
            return ed
        else:
            return len(A)
