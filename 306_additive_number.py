class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num or len(num) <= 2:
            return False

        for i in xrange(3, len(num) + 1):
            for nums in self.find_first_three_additive_nums(num[:i]):
                if nums:
                    j = i
                    l, r = nums[1], nums[2]
                    while j < len(num):
                        next = str(int(l) + int(r))
                        nlen = len(next)
                        if next == num[j: j + nlen]:
                            l, r = r, next
                            j += nlen
                        else:
                            break
                    else:
                        return True
        return False

    def find_first_three_additive_nums(self, num):
        n = len(num)
        for j in xrange(n - n / 3, n - n / 2 - 1, -1):
            if num[j] == '0' and len(num[j:]) != 1:
                continue
            for i in xrange(1, j):
                # leading zero
                if num[i] == '0' and len(num[i:j]) != 1:
                    continue
                if num[0] == '0' and len(num[:i]) != 1:
                    continue
                v1, v2, v3 = int(num[:i]), int(num[i:j]), int(num[j:])
                if v1 + v2 == v3:
                    yield v1, v2, v3
    
