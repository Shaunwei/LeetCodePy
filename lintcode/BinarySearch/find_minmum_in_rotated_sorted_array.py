class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        if not num:
            return -1

        st, ed = 0, len(num) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if num[st] < num[mid]:
                if num[mid] < num[ed]:
                    ed = mid
                else:
                    st = mid
            else:
                ed = mid
        return min(num[st], num[ed])


class Solution2:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        start, end = 0, len(num)-1
        while start + 1 < end:
            mid = (start + end) / 2
            if num[mid] >= num[end]:
                start = mid
            else:
                end = mid

        return min(num[start], num[end])
