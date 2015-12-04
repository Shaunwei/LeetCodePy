class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        5:00 - 5:12
        """
        # lookup table
        # converting based on strategy
        # special case 4, 9
        table = dict(zip([1, 5, 10, 50, 100, 500, 1000], list('IVXLCDM')))

        digit = 1000
        roman = ''
        while digit:
            val = num / digit
            num %= digit
            if 0 < val <= 3:
                roman += val * table[digit]
            elif val == 4:
                roman += table[digit] + table[5 * digit]
            elif 5 <= val <= 8:
                roman += table[5 * digit] + (val - 5) * table[digit]
            elif val == 9:
                roman += table[digit] + table[10 * digit]
            digit /= 10
        return roman

class Solution2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i2r = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        ret = ''
        digit = 1
        while num >= digit:
            val = num / digit % 10
            cur = ''
            if val <= 3:
                cur = i2r[digit] * val
            elif val == 4:
                cur = i2r[digit] + i2r[digit * 5]
            elif val <= 8:
                cur = i2r[digit * 5] + i2r[digit] * (val - 5)
            elif val == 9:
                cur = i2r[digit] + i2r[digit * 10]

            ret = cur + ret
            digit *= 10
        return ret
