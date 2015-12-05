class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if not A:
            return -1

        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if A[mid] == target:
                return mid
            elif A[st] < A[mid]:
                if A[st] <= target < A[mid]:
                    ed = mid
                else:
                    st = mid
            else:
                if A[mid] < target <= A[ed]:
                    st = mid
                else:
                    ed = mid
        if A[st] == target:
            return st
        elif A[ed] == target:
            return ed
        return -1