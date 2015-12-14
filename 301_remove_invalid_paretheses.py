class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # DFS
        # "()())"
        valid = collections.defaultdict(list)

        self.dfs(s, 0, 0, 0, valid, '', set(), 0)

        min_del = min(valid.keys())
        return valid[min_del]

    def dfs(self, s, pos, left, right, valid, temp, visited, delete):
        if (temp, pos, delete) in visited:
            return
        visited.add((temp, pos, delete))
        if pos == len(s) and left == right:
            valid[delete].append(temp)
            return
        if left < right or pos == len(s):
            return

        if s[pos] == '(':
            self.dfs(s, pos + 1, left + 1, right, valid, temp + '(', visited, delete)
            self.dfs(s, pos + 1, left, right, valid, temp, visited, delete + 1)
        elif s[pos] == ')':
            self.dfs(s, pos + 1, left, right + 1, valid, temp + ')', visited, delete)
            self.dfs(s, pos + 1, left, right, valid, temp, visited, delete + 1)
        else:
            self.dfs(s, pos + 1, left, right, valid, temp + s[pos], visited, delete)


class Solution2(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # BFS
        valid_parentheses = list()
        queue = collections.deque()
        queue.append(s)
        discovered = set()

        while queue and not valid_parentheses:
            size = len(queue)
            for _ in xrange(size):
                cur_str = queue.popleft()
                if self.is_valid(cur_str):
                    valid_parentheses.append(cur_str)
                    continue
                for new_str in self.remove_one_parenthese(cur_str):
                    if new_str not in discovered:
                        queue.append(new_str)
                        discovered.add(new_str)
        return valid_parentheses


    def remove_one_parenthese(self, s):
        for i in xrange(len(s)):
            if s[i] == '(' or s[i] == ')':
                yield s[:i] + s[i + 1:]

    def is_valid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
            else:
                # a-zA-Z
                pass
        return len(stack) == 0
