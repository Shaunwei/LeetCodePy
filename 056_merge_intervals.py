# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        ret = []
        curt = intervals[0]
        for interval in intervals[1:]:
            if curt.end < interval.start:
                ret.append(curt)
                curt = interval
            else:
                curt.end = max(curt.end, interval.end)
        ret.append(curt)
        return ret


class Solution1(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        curt = Interval(10**10, 10**10)
        merged = []
        for interval in intervals:
            if self.is_overlap(curt, interval):
                curt.start = min(curt.start, interval.start)
                curt.end = max(curt.end, interval.end)
            else:
                merged.append(curt)
                curt = interval
        merged.append(curt)
        return merged[1:]

    def is_overlap(self, ia, ib):
        if ia.start < ib.start and ia.end < ib.start:
            return False
        elif ib.start < ia.start and ib.end < ia.start:
            return False
        else:
            return True


class Solution2(object):
    def merge(self, intervals):
    ###
    # Merge Sort
        return self.merge_sort(intervals)

    def merge_sort(self, intervals):
        if len(intervals) == 1:
            return intervals

        length = len(intervals)
        left = self.merge_sort(intervals[:length / 2])
        right = self.merge_sort(intervals[length / 2:])
        return self.merge_intervals(left, right)

    def merge_intervals(self, left, right):
        merged = []
        MAX_INT = 2 ** 31 - 1
        l, r = 0, 0
        curt = Interval(MAX_INT, MAX_INT)
        while l < len(left) or r < len(right) or curt.start != MAX_INT:
            l_interval = left[l] if l < len(left) else Interval(MAX_INT, MAX_INT)
            r_interval = right[r] if r < len(right) else Interval(MAX_INT, MAX_INT)
            if l_interval.start < r_interval.start:
                l += 1
                if self.is_overlap(curt, l_interval):
                    curt.start = min(curt.start, l_interval.start)
                    curt.end = max(curt.end, l_interval.end)
                else:
                    merged.append(curt)
                    curt = l_interval
            else:
                r += 1
                if self.is_overlap(curt, r_interval):
                    curt.start = min(curt.start, r_interval.start)
                    curt.end = max(curt.end, r_interval.end)
                else:
                    merged.append(curt)
                    curt = r_interval
        return merged[1:]

    def is_overlap(self, ia, ib):
        if ia.start < ib.start:
            if ia.end < ib.start:
                return False
            else:
                return True
        else:
            if ib.end < ia.start:
                return False
            else:
                return True

