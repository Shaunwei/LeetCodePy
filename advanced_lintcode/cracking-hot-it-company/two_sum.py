class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    # Hash
    def twoSum(self, numbers, target):
        exist = {}
        for i, num in enumerate(numbers, 1):
            if target - num in exist:
                return [exist[target - num], i]
            exist[num] = i
        return []


class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    # two pointer
    def twoSum(self, numbers, target):
        entries = [[num, i] for i, num in enumerate(numbers, 1)]
        entries.sort()

        i, j = 0, len(entries) - 1
        while i < j:
            vi, vj = entries[i][0], entries[j][0]
            if vi + vj == target:
                l, r = entries[i][1], entries[j][1]
                return [min(l, r), max(l, r) ]
            elif vi + vj < target:
                i += 1
            else:
                j -= 1
        return []


class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    # sort
    def twoSum(self, numbers, target):
        entries = [[num, i] for i, num in enumerate(numbers, 1)]
        entries.sort()

        ed = len(entries) - 1
        for st, (num, i) in enumerate(entries):
            j = self.bs(entries, target - num, st + 1, ed)
            if j != -1:
                return [min(i, j), max(i, j)]
        return []

    def bs(self, entries, target, st, ed):
        while st + 1 < ed:
            mid = (st + ed) / 2
            if entries[mid][0] == target:
                return entries[mid][1]
            elif entries[mid][0] < target:
                st = mid
            else:
                ed = mid
        if entries[st][0] == target:
            return entries[st][1]
        elif entries[ed][0] == target:
            return entries[ed][1]
        else:
            return -1
