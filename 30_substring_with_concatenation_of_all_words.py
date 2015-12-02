import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []

        word_dict = collections.defaultdict(int)
        for word in words:
            word_dict[word] += 1

        wcnt, wlen = len(words), len(words[0])
        ret = []
        for i in xrange(len(s) - wlen * wcnt + 1):
            if self.is_valid(s[i: i + wlen * wcnt], wlen, word_dict):
                ret.append(i)
        return ret

    def is_valid(self, s, wlen, wdict):
        mdict = wdict.copy()
        for i in xrange(0, len(s), wlen):
            word = s[i: i + wlen]
            if mdict[word] <= 0:
                return False
            mdict[word] -= 1
        return True


class Solution2:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        wlen = len(words[0])
        num_words = len(words)
        if len(s) < num_words * wlen:
            return []

        indices = []
        for i in xrange(0, len(s) - num_words*wlen + 1):
            subs = [s[j: j + wlen] for j in range(i, i + (num_words-1)*wlen + 1, wlen)]
            for word in words:
                if word not in subs:
                    break
                subs.remove(word)
            else:
                indices.append(i)
        return indices


