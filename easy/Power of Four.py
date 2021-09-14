import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 0.03295203298330307
        # x = 1
        # while x <= n:
        #     if x == n:
        #         return True
        #     x *= 4
        # return False

        # code refactoring (R) - 0.0229679923504591
        # if n < 1:
        #     return False
        # while n % 4 == 0:
        #     n //= 4
        # return n == 1

        # code refactoring (R) - 0.03167635761201382
        # return n > 0 and math.log(n, 4).is_integer()

        # code refactoring (R) - 0.03341268561780453
        # return n > 0 and math.log(n, 4) % 1 == 0

        # code refactoring (R) - 0.020520655438303947
        if n == 1:
            return True
        return n > 0 and n & 0xaaaaaaaa == 0 and n & (n-1) == 0


s = Solution()
# print(s.isPowerOfFour(16))
# print(s.isPowerOfFour(1))
# print(s.isPowerOfFour(0))
# print(s.isPowerOfFour(8))
print(s.isPowerOfFour(10))
print(s.isPowerOfFour(3))
print(s.isPowerOfFour(-1))


if __name__ == '__main__':
    from timeit import Timer
    query = [0, 1, 3, 8, 10, 16, -1, 30020, 300001]
    t = Timer(f"for t in {query}: Solution().isPowerOfFour(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

