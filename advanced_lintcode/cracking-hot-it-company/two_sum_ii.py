class BST:
    count = 0
    def __init__(self, val, cnt=0):
        self.val = val
        self.cnt = cnt
        self.left = self.right = None

    @staticmethod
    def build(nums, st, ed):
        if st > ed:
            return

        mid = (st + ed) / 2
        root = BST(nums[mid])
        root.right = BST.build(nums, mid + 1, ed)
        root.cnt = BST.count
        BST.count += 1
        root.left = BST.build(nums, st, mid - 1)
        return root

    def query_larger(self, root, target):
        prev = None
        while root:
            if root.val > target:
                prev = root
                root = root.left
            elif root.val < target:
                prev = root
                root = root.right
            else:
                return root.cnt
        if prev.val < target:
            return prev.cnt
        else:
            return prev.cnt + 1


class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer

    # BST
    def twoSum2(self, nums, target):
        nums.sort()
        root = BST.build(nums, 0, len(nums) - 1)

        cnts = 0
        for num in nums:
            cnt = root.query_larger(root, target - num)
            if num > target - num:
                cnt -= 1
            cnts += cnt
        return cnts / 2


class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer

    # # two pointers
    def twoSum2(self, nums, target):
        nums.sort()
        cnts = 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                cnts += j - i
                j -= 1
            else:
                i += 1
        return cnts
