import heapq

class Building:
    def __init__(self, args):
        self.st = args[0]
        self.ed = args[1]
        self.height = args[2]
        self.done = False

    def __cmp__(self, other):
        return -1 * (self.height - other.height)

    def is_ending(self, val):
        return self.ed == val

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        bs = map(Building, buildings)
        pos_heap = []
        for b in bs:
            heapq.heappush(pos_heap, (b.st, b))
            heapq.heappush(pos_heap, (b.ed, b))

        skyline = []
        active = []
        while pos_heap:
            pos, b = heapq.heappop(pos_heap)
            if b.is_ending(pos):
                b.done = True
            else:
                heapq.heappush(active, b)

            while active and active[0].done:
                heapq.heappop(active)
            height = active[0].height if active else 0
            if skyline:
                if skyline[-1][1] != height:
                    if skyline[-1][0] != pos:
                        skyline.append([pos, height])
                    else:
                        skyline[-1][1] = height
            else:
                skyline.append([pos, height])
        return skyline

if __name__ == '__main__':

    print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
