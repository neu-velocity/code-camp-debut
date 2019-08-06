# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if isBadVersion(mid) == False:
                start = mid
            elif isBadVersion(mid) == True and isBadVersion(mid - 1) == False and isBadVersion(mid + 1) == True:
                return mid
            else:
                end = mid

        
        if isBadVersion(start) == True:
            return start
        if isBadVersion(end) == True:
            return end