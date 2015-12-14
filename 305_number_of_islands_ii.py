class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        self.uf = UnionFind(m, n)

        for i, j in positions:
            self.add_land(i, j)
            ret.append(self.count_lands())
        return ret

    def add_land(self, i, j):
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            self.uf.union(i, j, i + dx, j + dy)

    def count_lands(self):
        return self.uf.count

class UnionFind:
    def __init__(self, m, n):
        self.parent = {}
        self.m = m
        self.n = n
        self.size = {}
        self.count = 0

    def add(self, i, j):
        self.parent[(i, j)] = (i, j)
        self.size[(i, j)] = 1
        self.count += 1

    def union(self, i, j, oi, oj):
        if (i, j) not in self.parent:
            self.add(i, j)

        if not (0 <= oi < self.m and 0 <= oj < self.n):
            return
        if (oi, oj) not in self.parent:
            return

        p0 = self.find(i, j)
        p1 = self.find(oi, oj)
        if p0 == p1:
            return

        if self.size[p0] < self.size[p1]:
            self.parent[p0] = p1
            self.size[p1] += self.size[p0]
            self.count -= 1
        else:
            self.parent[p1] = p0
            self.size[p0] += self.size[p1]
            self.count -= 1

    def find(self, *p):
        while self.parent[p] != p:
            temp = self.parent[p]
            self.parent[p] = self.parent[temp]
            p = temp
        return p



        
