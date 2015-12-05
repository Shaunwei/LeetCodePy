"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        ed = 1
        while reader.get(ed) != -1 and reader.get(ed) < target:
            ed *= 2

        st = 0
        while st + 1 < ed:
            mid = (st + ed) / 2
            mid_val = reader.get(mid)
            if mid_val == target:
                ed = mid
            elif mid_val < target:
                st = mid
            else:
                ed = mid
        if reader.get(st) == target:
            return st
        elif reader.get(ed) == target:
            return ed
        return -1


class Solution2:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        if reader.get(0) == -1:
            return -1
        st = 0
        ed = self.find_end(reader, target)
        # first pos
        while st + 1 < ed:
            mid = (st + ed) / 2
            val = reader.get(mid)
            if val == target:
                ed = mid
            elif val < target:
                st = mid
            else:
                ed = mid

        if reader.get(st) == target:
            return st
        elif reader.get(ed) == target:
            return ed
        else:
            return -1

    def find_end(self, reader, target):
        ed = 1
        while reader.get(ed) < target and reader.get(ed) != -1:
            ed *= 2
        return ed
