# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(n, target):
    return n >= target


class Solution(object):
    # def firstBadVersion(self, n):
    # isBadVersion 사용을 위해 target parameter 추가
    def firstBadVersion(self, n, t):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        mid = (high + 1) // 2
        while low+1 != high:
            if isBadVersion(mid, t):
                high = mid
                mid = (high - low + 1) // 2
            else:
                low = mid
                mid = (high - low + 1) // 2 + low
        return high


s = Solution()
# print(s.firstBadVersion(5, 4))
# print(s.firstBadVersion(1, 1))
# print(s.firstBadVersion(10, 1))
# print(s.firstBadVersion(14, 1))
# print(s.firstBadVersion(14, 14))
print(s.firstBadVersion(200, 170))
print(s.firstBadVersion(2126753390, 1702766719))
