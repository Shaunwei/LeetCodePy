#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        st, ed = 0, n
        while st + 1 < ed:
            mid = (st + ed) / 2
            if SVNRepo.isBadVersion(mid):
                ed = mid
            else:
                st = mid
        if SVNRepo.isBadVersion(st):
            return st
        else:
            return ed
