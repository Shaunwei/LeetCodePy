class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        ret = [-1, -1]
        if not A:
            return ret

        ret[0] = self.search_first(A, target)
        ret[1] = self.search_last(A, target)
        return ret

    def search_first(self, A, target):
        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if A[mid] == target:
                ed = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[st] == target:
            return st
        elif A[ed] == target:
            return ed
        return -1

    def search_last(self, A, target):
        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if A[mid] == target:
                st = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[ed] == target:
            return ed
        elif A[st] == target:
            return st
        return -1



class Solution2:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        ret = [-1, -1]
        if not A:
            return ret

        # find the first position of target
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            ret[0] = start
        elif A[end] == target:
            ret[0] = end

        # find the last position of target
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            ret[1] = end
        elif A[start] == target:
            ret[1] = start

        return ret

