# allow to modify grid
class Solution0(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num += 1
                    self.dfs(grid, i, j)
        return num

    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == '1':
                grid[i][j] = '0'
            else:
                return
        else:
            return

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


import collections
class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num += 1
                    self.bfs(grid, i, j)
        return num

    def bfs(self, grid, i, j):
        queue = collections.deque()
        queue.append((i, j))
        grid[i][j] = '0'
        while queue:
            mi, mj = queue.popleft()
            if mi > 0 and grid[mi - 1][mj] == '1':
                grid[mi - 1][mj] = '0'
                queue.append((mi - 1, mj))
            if mj > 0 and grid[mi][mj - 1] == '1':
                grid[mi][mj - 1] = '0'
                queue.append((mi, mj - 1))
            if mi < len(grid) - 1 and grid[mi + 1][mj] == '1':
                grid[mi + 1][mj] = '0'
                queue.append((mi + 1, mj))
            if mj < len(grid[0]) - 1 and grid[mi][mj + 1] == '1':
                grid[mi][mj + 1] = '0'
                queue.append((mi, mj + 1))


# not allow to modify grid
class Solution2:
    class UnionFind:
        def __init__(self, grid):
            self.num = 0
            self.m, self.n = len(grid), len(grid[0])
            self.grid = {}

        def union(self, i1, j1, i2, j2):
            if not (0 <= i2 < self.m and 0 <= j2 < self.n):
                return
            if (i1, j1) not in self.grid:
                self.num += 1
                self.grid[(i1, j1)] = (i1, j1)

            if (i2, j2) not in self.grid:
                return

            p1 = self.find(i1, j1)
            p2 = self.find(i2, j2)
            if p1 == p2:
                return
            if p1 < p2:
                self.grid[p2] = p1
            else:
                self.grid[p1] = p2
            self.num -= 1

        def find(self, *p):
            while self.grid[p] != p:
                mp = self.grid[p]
                self.grid[p] = self.grid[mp]
                p = mp
            return p

    def numIslands(self, grid):
        uf = Solution2.UnionFind(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        uf.union(i, j, i + dx, j + dy)
        for i in sorted(uf.grid.items()):
            print(i)
        return uf.num


class Solution3(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.dfs(grid, i, j, visited)
                    num += 1
        return num

    def dfs(self, grid, i, j, visited):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == '1' and (i, j) not in visited:
                visited.add((i, j))
            else:
                return
        else:
            return
        self.dfs(grid, i + 1, j, visited)
        self.dfs(grid, i, j + 1, visited)
        self.dfs(grid, i - 1, j, visited)
        self.dfs(grid, i, j - 1, visited)

import collections
class Solution4(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        discovered = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in discovered:
                    self.bfs(grid, i, j, discovered)
                    num += 1
        return num

    def bfs(self, grid, i, j, discovered):
        queue = collections.deque()
        queue.append((i, j))
        discovered.add((i, j))
        while queue:
            mi, mj = queue.popleft()
            for di, dj in (0, -1), (-1, 0), (0, 1), (1, 0):
                if 0 <= mi + di < len(grid) and 0 <= mj + dj < len(grid[0]):
                    if grid[mi + di][mj + dj] == '1' and \
                        (mi + di, mj + dj) not in discovered:
                        discovered.add((mi + di, mj + dj))
                        queue.append((mi + di, mj + dj))

if __name__ == '__main__':
    grid = ["1111111","0000001", "1111101","1000101","1010101","1011101", "1111111"]
    print(Solution2().numIslands(grid))
