import math


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            log_n = round(math.log(n, 2), 14)
            return True if log_n % int(log_n) == 0 else False


s = Solution()
# print(s.isPowerOfTwo(1))
# print(s.isPowerOfTwo(2))
# print(s.isPowerOfTwo(7))
# print(s.isPowerOfTwo(8))
# print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(536870912))
# print(s.isPowerOfTwo(511))
print(s.isPowerOfTwo(32767))
print(s.isPowerOfTwo(-1))
