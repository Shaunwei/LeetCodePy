class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        ret = []
        self.gen_pairs(n, n, ret, [])
        return ret

    def gen_pairs(self, l, r, ret, tmp):
        if l == r == 0:
            ret.append(''.join(tmp))
            return
        if l < 0 or r < 0:
            return

        if l < r:
            tmp.append(')')
            self.gen_pairs(l, r - 1, ret, tmp)
            tmp.pop()
        tmp.append('(')
        self.gen_pairs(l - 1, r, ret, tmp)
        tmp.pop()


class Solution2:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return []

        self.res = set()
        self.comb(n, 0, 0, '')
        return list(self.res)

    def comb(self, n, paired, unpaired, temp):
        if paired + unpaired == n:
            self.res.add(temp + unpaired * ')')
            return

        self.comb(n, paired, unpaired + 1, temp + '(')
        # pair it conditionally
        ## WRONG: self.comb(n, paired + 1, unpaired, temp + '()')
        ## this case will ingnore some pair just has ')'
        if unpaired > 0:
            self.comb(n, paired + 1, unpaired - 1, temp + ')')

    def comb1(self, n, l, r, temp):
        if l == r == n:
            self.res.append(temp)
            return
        if l < n:
            self.comb1(n, l + 1, r, temp + '(')
        if r < l <= n:
            self.comb1(n, l, r + 1, temp + ')')