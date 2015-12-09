"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # one queue
        ret = []
        if not root:
            return ret

        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            lvl = []
            for _ in xrange(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                lvl.append(node.val)
            ret.append(lvl)
        return ret


class Solution2:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # dfs with pos indicator
        lvl_dict = collections.defaultdict(list)
        self.dfs(root, 0, 0, lvl_dict)

        ret = []
        for lvl in sorted(lvl_dict.keys()):
            level = []
            for _, val in sorted(lvl_dict[lvl]):
                level.append(val)
            ret.append(level)
        return ret

    def dfs(self, root, lvl, pos, lvl_dict):
        if root:
            lvl_dict[lvl].append([pos, root.val])
            self.dfs(root.left, lvl + 1, pos - 1, lvl_dict)
            self.dfs(root.right, lvl + 1, pos + 1, lvl_dict)


class Solution3:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # dfs
        lvl_dict = collections.defaultdict(list)
        self.dfs(root, 0, lvl_dict)
        ret = []
        for lvl in sorted(lvl_dict.keys()):
            ret.append(lvl_dict[lvl])
        return ret

    def dfs(self, root, lvl, lvl_dict):
        if root:
            lvl_dict[lvl].append(root.val)
            self.dfs(root.left, lvl + 1, lvl_dict)
            self.dfs(root.right, lvl + 1, lvl_dict)
