class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return a or b

        carry = 0
        a = a[::-1]
        b = b[::-1]
        i = 0
        ret = ''
        while i < len(a) or i < len(b) or carry:
            va = int(a[i]) if i < len(a) else 0
            vb = int(b[i]) if i < len(b) else 0
            val = va + vb + carry
            ret += str(val % 2)
            carry = val / 2
            i += 1
        return ret[::-1]


class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return a or b

        ret = ''
        ia = len(a) - 1
        ib = len(b) - 1
        carry = 0
        while ia >= 0 or ib >= 0:
            va = int(a[ia]) if ia >= 0 else 0
            vb = int(b[ib]) if ib >= 0 else 0
            ret = str((va + vb + carry) % 2) + ret
            carry = (va + vb + carry) / 2
            ia -= 1
            ib -= 1
        if carry:
            ret = str(carry) + ret
        return ret