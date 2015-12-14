class Solution(object):
    def fullJustify(self, words, L):
        """
        :type words: List[str]
        :type L: int
        :rtype: List[str]
        """
        if not words or not L:
            return ['']

        ret = []
        cur = []
        length = 0
        for word in words:
            # at least one space in between
            if length + len(word) + len(cur) <= L:
                cur.append(word)
                length += len(word)
            else:
                ret.append(self.full_justify(cur, length, L))
                cur = [word]
                length = len(word)
        if cur:
            ret.append(self.left_justify(cur, length, L))
        return ret

    def full_justify(self, words, length, L):
        if len(words) == 1:
            return self.left_justify(words, length, L)

        gaps = len(words) - 1
        spaces = (L - length) / gaps
        extras = (L - length) % gaps
        line = words[0]
        for i, word in enumerate(words[1:]):
            if extras > 0:
                line += ' ' * spaces + ' ' + word
                extras -= 1
            else:
                line += ' ' * spaces + word
        return line

    def left_justify(self, words, length, L):
        return ' '.join(words) + ' ' * (L - length - (len(words) - 1))
