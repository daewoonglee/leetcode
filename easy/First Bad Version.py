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
        # 1.7130007939995266
        # low = 0
        # high = n
        # mid = (high + 1) // 2
        # while low+1 != high:
        #     if isBadVersion(mid, t):
        #         high = mid
        #         mid = (high - low + 1) // 2
        #     else:
        #         low = mid
        #         mid = (high - low + 1) // 2 + low
        # return high

        # 0.2262335770064965
        low = 1
        high = n
        while low != high:
            mid = (low + high) // 2
            if isBadVersion(mid, t):
                high = mid
            else:
                low = mid + 1
        return low


s = Solution()
print(s.firstBadVersion(5, 4))
print(s.firstBadVersion(1, 1))
print(s.firstBadVersion(10, 1))
print(s.firstBadVersion(14, 1))
print(s.firstBadVersion(14, 14))
print(s.firstBadVersion(200, 170))
print(s.firstBadVersion(2126753390, 1702766719))
print(s.firstBadVersion(21267533900, 17027667190))


if __name__ == '__main__':
    from timeit import Timer
    query = [[5, 4],
             [1, 1],
             [10, 1],
             [14, 1],
             [14, 14],
             [200, 170],
             [2126753390, 1702766719],
             [21267533900, 17027667190]]
    t = Timer(f"for t in {query}: Solution().firstBadVersion(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
