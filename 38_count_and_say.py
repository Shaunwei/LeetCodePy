class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''

        say = '1'
        for _ in range(n - 1):
            cnt = 0
            tmp = ''
            say += '$'
            for i in range(len(say)):
                if i == 0 or say[i - 1] == say[i]:
                    cnt += 1
                else:
                    tmp += str(cnt) + say[i - 1]
                    cnt = 1
            say = tmp
        return say



class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        Two pointers algorithm: FIND NEXT DIFFERENT
        """
        if n <= 0:
            return ''

        say = '1'
        for _ in range(n - 1):
            temp = ''
            count = 1
            for i in range(1, len(say)):
                if say[i] == say[i - 1]:
                    count += 1
                else:
                    temp += str(count) + say[i - 1]
                    count = 1
            temp += str(count) + say[-1]
            say = temp
        return say

