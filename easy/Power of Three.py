class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 0.099209257
        # t = 1
        # while t <= n:
        #     if n == t:
        #         return True
        #     t *= 3
        # return False

        # code refactoring (R) 01 - 0.042821463000000004
        # if n < 1:
        #     return False
        # while n % 3 == 0:
        #     n //= 3
        # return n == 1

        # code refactoring (R) 02 - 0.40979566
        # if n < 1:
        #     return False
        # pattern = re.compile("^10*$")
        # return bool(pattern.match(np.base_repr(n, base=3)))

        # code refactoring (R) 03 - 0.05994646000000001
        # if n < 1:
        #     return False
        # return (math.log10(n) / math.log10(3) % 1) == 0

        # code refactoring (R) 04 - 0.026959229
        return n > 0 and 1162261467 % n == 0            

s = Solution()
# print(s.isPowerOfThree(27))
# print(s.isPowerOfThree(0))
# print(s.isPowerOfThree(45))
# print(s.isPowerOfThree(243))
print(s.isPowerOfThree(1))


if __name__ == '__main__':
    from timeit import Timer
    query = [27, 0, 45, 243, 1, 1000, 30000, 3333, 24443, 1112344553, 33333333333, -27, -243, -1000,
             -30000, -1112344553]
    t = Timer(f"for t in {query}: Solution().isPowerOfThree(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

