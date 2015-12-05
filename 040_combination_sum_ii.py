class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target <= 0:
            return []

        ret = []
        candidates.sort()
        self.comb(candidates, 0, target, ret, [])
        return ret

    def comb(self, vals, pos, target, ret, tmp):
        if target == 0:
            ret.append(tmp[:])
            return
        if target < 0 or pos >= len(vals):
            return

        for i in xrange(pos, len(vals)):
            # remove dup
            if i > pos and vals[i] == vals[i - 1]:
                continue

            tmp.append(vals[i])
            self.comb(vals, i + 1, target - vals[i], ret, tmp)
            tmp.pop()

class Solution2(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        self.comb(candidates, target, ret, [])
        return ret

    def comb(self, cands, target, ret, tmp):
        if target == 0:
            ret.append(tmp[:])
            return
        if not cands or target < 0:
            return

        for i, val in enumerate(cands):
            if i > 0 and cands[i] == cands[i - 1]:
                continue
            self.comb(cands[i + 1:], target - val, ret, tmp + [val])

