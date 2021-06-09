class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # def factorial(n):
        #     if n <= 1:
        #         return 1
        #     return n * factorial(n-1)
        # fn = str(factorial(n))
        # # 9.148081381
        # cnt = 0
        # for i in range(len(fn)):
        #     if fn[-1-i] != "0":
        #         break
        #     cnt += 1
        # return cnt

        # code refactoring - 0.24867132100000003
        # import math
        # return sum([n//(5**i) for i in range(1, int(math.log(n, 5))+1)]) if n else 0

        # code refactoring (R) - 0.076444951
        cnt = 0
        while n != 0:
            n //= 5
            cnt += n
        return cnt


s = Solution()
print(s.trailingZeroes(0))
# print(s.trailingZeroes(3))
# print(s.trailingZeroes(4))
# print(s.trailingZeroes(5))
# print(s.trailingZeroes(7))
# print(s.trailingZeroes(9))
# print(s.trailingZeroes(10))
# print(s.trailingZeroes(15))
# print(s.trailingZeroes(24))
# print(s.trailingZeroes(29))
# print(s.trailingZeroes(30))
# print(s.trailingZeroes(50))
# print(s.trailingZeroes(100))
print(s.trailingZeroes(624))
print(s.trailingZeroes(625))
print(s.trailingZeroes(825))


if __name__ == '__main__':
    from timeit import Timer
    query = [0, 3, 4, 5, 7, 9, 10, 15, 24, 29, 30, 50, 100, 624, 625, 825]
    t = Timer(f"for t in {query}: Solution().trailingZeroes(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
