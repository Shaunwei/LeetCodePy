class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        if not A or len(A) < 3:
            return -1

        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if A[mid - 1] < A[mid]:
                if A[mid] > A[mid + 1]:
                    return mid
                else:
                    st = mid
            else:
                ed = mid

        if A[st] > A[ed]:
            return st
        elif A[st] < A[ed]:
            return ed
        return -1

class Solution2:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        start, end = 0, len(A)-1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] < A[mid+1]:
                start = mid
            elif A[mid-1] > A[mid] > A[mid+1]:
                end = mid
            elif A[mid-1] > A[mid] and A[mid] < A[mid+1]:
                start = mid
            else:
                raise Exception('non-exist state')

        if A[start] > A[end]:
            return start
        else:
            return end
