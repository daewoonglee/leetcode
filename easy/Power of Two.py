import math


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 0.13976284
        # if n == 1:
        #     return True
        # elif n < 1:
        #     return False
        # else:
        #     log_n = round(math.log(n, 2), 14)
        #     return True if log_n % int(log_n) == 0 else False

        # code refactoring (R) - 0.0359792
        # if n == 0:
        #     return False
        # return True if not n & (n-1) else False
        return False if n == 0 or n & (n-1) else True


s = Solution()
print(s.isPowerOfTwo(0))    # T
# print(s.isPowerOfTwo(1))    # T
# print(s.isPowerOfTwo(2))    # T
print(s.isPowerOfTwo(6))    # F
# print(s.isPowerOfTwo(7))    # F
# print(s.isPowerOfTwo(8))    # T
# print(s.isPowerOfTwo(16))   # T
print(s.isPowerOfTwo(536870912))    # T
# print(s.isPowerOfTwo(511))
print(s.isPowerOfTwo(32767))    # f
print(s.isPowerOfTwo(-1))   # f


if __name__ == '__main__':
    from timeit import Timer
    query = [0, 1, 2, 6, 7, 8, 16, 536870912, 511, 32767, -1]
    t = Timer(f"for t in {query}: Solution().isPowerOfTwo(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
