class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # Binary Search
        discover = {(x, y)}
        loc = {'x': set(), 'y': set()}
        queue = collections.deque()
        queue.append((x, y))
        while queue:
            mx, my = queue.popleft()
            for nx, ny in self.bs_gen(image, mx, my):
                if (nx, ny) not in discover:
                    queue.append((nx, ny))
                    discover.add((nx, ny))
            loc['x'].add(mx)
            loc['y'].add(my)
        print(loc)
        return (max(loc['x']) - min(loc['x']) + 1) * (max(loc['y']) - min(loc['y']) + 1)

    def bs_gen(self, image, x, y):
        yield self.bs_top(image, x, y)
        yield self.bs_down(image, x, y)
        yield self.bs_left(image, x, y)
        yield self.bs_right(image, x, y)

    def bs_top(self, image, x, y):
        st, ed = 0, x
        while st + 1 < ed:
            mid = (st + ed) / 2
            if '1' in image[mid]:
                ed = mid
            else:
                st = mid
        if '1' in image[st]:
            return (st, y)
        return (ed, y)

    def bs_down(self, image, x, y):
        st, ed = x, len(image) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if '1' in image[mid]:
                st = mid
            else:
                ed = mid
        if '1' in image[ed]:
            return (ed, y)
        return (st, y)

    def bs_left(self, image, x, y):
        st, ed = 0, y
        while st + 1 < ed:
            mid = (st + ed) / 2
            if '1' in (image[i][mid] for i in xrange(len(image))):
                ed = mid
            else:
                st = mid
        if '1' in (image[i][st] for i in xrange(len(image))):
            return (x, st)
        return (x, ed)

    def bs_right(self, image, x, y):
        st, ed = y, len(image[0]) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if '1' in (image[i][mid] for i in xrange(len(image))):
                st = mid
            else:
                ed = mid
        if '1' in (image[i][ed] for i in xrange(len(image))):
            return (x, ed)
        return (x, st)


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # DFS
        loc = {'x': set(), 'y': set()}
        self.dfs(image, x, y, loc, set())
        return (max(loc['x']) - min(loc['x']) + 1) * (max(loc['y']) - min(loc['y']) + 1)

    def dfs(self, image, x, y, loc, visited):
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
            return
        if (x, y) in visited or image[x][y] == '0':
            return
        visited.add((x, y))
        loc['x'].add(x)
        loc['y'].add(y)

        self.dfs(image, x + 1, y, loc, visited)
        self.dfs(image, x, y + 1, loc, visited)
        self.dfs(image, x - 1, y, loc, visited)
        self.dfs(image, x, y - 1, loc, visited)
