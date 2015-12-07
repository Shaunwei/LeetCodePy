class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]

        carry = 1
        for i in xrange(len(digits) - 1, -1, -1):
            val = digits[i]
            digits[i] = (val + carry) % 10
            carry = (val + carry) / 10
        if carry:
            digits.insert(0, carry)
        return digits
