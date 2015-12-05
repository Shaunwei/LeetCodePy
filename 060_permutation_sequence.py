class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n <= 0:
            return ''

        nums = range(1, n + 1)
        for _ in range(k - 1):
            nums = self.next_perm(nums)
        return ''.join(map(str, nums))

    def next_perm(self, nums):
        # 231 -> 312
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            return nums[::-1]

        for j in xrange(len(nums) - 1, -1, -1):
            if nums[i] < nums[j]:
                break

        nums[i], nums[j] = nums[j], nums[i]

        m, n = i + 1, len(nums) - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        return nums


class Solution2(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
    #     ret = []
    #     self.perm(range(1, n + 1), ret, [])
    #     return ''.join(map(str, ret[k - 1]))

    # def perm(self, nums, ret, tmp):
    #     if not nums:
    #         ret.append(tmp[:])
    #         return
    #     for i, num in enumerate(nums):
    #         self.perm(nums[:i] + nums[i + 1:], ret, tmp + [num])
        result = ''
        k -= 1
        factorial = math.factorial(n-1)
        num = [i for i in xrange(1, n+1)]
        for i in reversed(xrange(n)):
            cur = num[k/factorial]
            result += str(cur)
            num.remove(cur)
            if i != 0:
                k %= factorial
                factorial /= i
        return result