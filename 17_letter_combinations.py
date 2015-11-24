class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # do combination
        # for loops!
        if not digits:
            return []

        table = { 1: [''], 0: [''], 2: list('abc'), 3: list('def'), 4: list('ghi'), 5: list('jkl'),
                  6: list('mno'), 7: list('pqrs'), 8: list('tuv'), 9: list('wxyz')}

        ret = ['']
        for digit in digits:
            temp = []
            for comb in ret:
                for char in table[int(digit)]:
                    temp.append(comb + char)
            ret = temp
        return ret

class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi',
                 '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        return reduce(lambda acc, d: [a + s for a in acc for s in table[d]], digits, [''])