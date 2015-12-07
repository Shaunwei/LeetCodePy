# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        MAX_INT = 2**31 - 1
        dummy = Interval(MAX_INT, MAX_INT)
        intervals.append(dummy)
        merged = []
        for i, interval in enumerate(intervals):
            if self.is_overlap(interval, newInterval):
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
            else:
                if interval.end < newInterval.start:
                    merged.append(interval)
                else:
                    merged.append(newInterval)
                    merged.extend(intervals[i:])
                    break
        # dummy end
        merged.pop()
        return merged

    def is_overlap(self, ia, ib):
        if ia.start < ib.start and ia.end < ib.start:
            return False
        elif ib.start < ia.start and ib.end < ia.start:
            return False
        else:
            return True



class Solution2(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ret = []
        insert_pos = 0
        for i, interval in enumerate(intervals):
            if interval.end < newInterval.start:
                insert_pos += 1
                ret.append(interval)
            elif interval.start > newInterval.end:
                ret.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        ret.insert(insert_pos, newInterval)
        return ret

