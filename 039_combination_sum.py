class Solution(object):
    def combinationSum(self, candidates, target):
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
            tmp.append(vals[i])
            self.comb(vals, i, target - vals[i], ret, tmp)
            tmp.pop()

class Solution2(object):
    def combinationSum(self, candidates, target):
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
            self.comb(cands[i:], target - val, ret, tmp + [val])
