class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: {'in': set(), 'out': set()} for i in xrange(numCourses)}
        for c, d in prerequisites:
            graph[c]['in'].add(d)
            graph[d]['out'].add(c)

        order = []
        queue = collections.deque()
        finished = set()
        for i in xrange(numCourses):
            if not graph[i]['in']:
                queue.append(i)
                finished.add(i)

        while queue:
            c = queue.popleft()
            for p in graph[c]['out']:
                graph[p]['in'].remove(c)
                if not graph[p]['in'] and p not in finished:
                    finished.add(p)
                    queue.append(p)
            order.append(c)
        if len(order) == numCourses:
            return order
        return []
