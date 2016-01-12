class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        cnts = 0
        S.sort()

        for i, l in enumerate(S):
            j, k = 0, i - 1
            while j < k:
                if S[j] + S[k] > l:
                    cnts += k - j
                    k -= 1
                else:
                    j += 1
        return cnts
