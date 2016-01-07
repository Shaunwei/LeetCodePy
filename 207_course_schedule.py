class Solution0(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # no incoming edges
        graph = {i: set() for i in xrange(numCourses)}
        for c, dep in prerequisites:
            graph[c].add(dep)

        can_finish = [False] * numCourses
        queue = collections.deque()
        for i, deps in graph.items():
            if not deps:
                queue.append(i)
                can_finish[i] = True

        while queue:
            course = queue.popleft()
            graph.pop(course)
            for c, dep in graph.items():
                if course in dep:
                    dep.remove(course)
                if not dep and not can_finish[c]:
                    can_finish[c] = True
                    queue.append(c)
        return len(graph) == 0

class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # no incoming edges (opt)
        # 10x faster than previous
        graph = {i: {'in': set(), 'out': set()} for i in xrange(numCourses)}
        for c, dep in prerequisites:
            graph[c]['in'].add(dep)
            graph[dep]['out'].add(c)

        can_finish = [False] * numCourses
        queue = collections.deque()
        for i in xrange(numCourses):
            if not graph[i]['in']:
                can_finish[i] = True
                queue.append(i)

        while queue:
            course = queue.popleft()
            for c in graph[course]['out']:
                graph[c]['in'].remove(course)
                if not graph[c]['in'] and not can_finish[c]:
                    can_finish[c] = True
                    queue.append(c)
        return all(can_finish)


class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # dfs
        graph = {i: set() for i in xrange(numCourses)}
        for c, dep in prerequisites:
            graph[c].add(dep)

        visited = set()
        for c in xrange(numCourses):
            if c not in visited and not self.dfs_has_no_cycle(graph, c, visited, set()):
                return False
        return True

    def dfs_has_no_cycle(self, graph, course, visited, marked):
        if course in marked:
            return False
        marked.add(course)
        for dep in graph[course]:
            if dep not in visited and not self.dfs_has_no_cycle(graph, dep, visited, marked):
                return False
        marked.remove(course)
        visited.add(course)
        return True
