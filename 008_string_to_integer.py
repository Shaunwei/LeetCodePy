__author__ = 'shawei'
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 3:29 - 3:38
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31
        string = str.strip()
        if not string:
            return 0
        vals = []
        for s in string:
            if not vals and s in '+-':
                vals.append(s)
            elif s.isdigit():
                vals.append(s)
            else:
                break

        if len(vals) == 1 and vals[0] in '+-':
            return 0
        if vals:
            val = int(''.join(vals))
            if val > MAX_INT:
                return MAX_INT
            elif val < MIN_INT:
                return MIN_INT
            else:
                return val
        return 0

class Solution2(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        num = ''
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        for i, char in enumerate(str):
            if (i == 0 and char in '+-') or '0' <= char <= '9':
                num += char
            else:
                # return valid
                break

        if num in '+-':
            return 0
        elif MIN_INT <= int(num) <= MAX_INT:
            return int(num)
        elif int(num) > MAX_INT:
            return MAX_INT
        else:
            return MIN_INT
