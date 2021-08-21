class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 0.08953687099999999
        # primes = [5, 3, 2]
        # idx = 0
        # while n:
        #     while n != 1:
        #         q, d = divmod(n, primes[idx])
        #         if d != 0:
        #             break
        #         n = q
        #     idx += 1
        #     if idx > 2:
        #         break
        # return True if n == 1 else False

        # code refactoring 01 - 0.06915089199999999
        # for p in [5, 3, 2]:
        #     while n > 1:
        #         q, d = divmod(n, p)
        #         if d != 0:
        #             break
        #         n = q
        # return n == 1

        # code refactoring (R) 02 - 0.041218319
        if n < 2:
            return False
        for p in [5, 3, 2]:
            while n % p == 0:
                n //= p
        return n == 1


s = Solution()
print(s.isUgly(10))
print(s.isUgly(60))
print(s.isUgly(61))
print(s.isUgly(61111))
print(s.isUgly(0))
print(s.isUgly(5000))


if __name__ == '__main__':
    from timeit import Timer
    query = [10, 60, 61, 61111, 0, 5000]
    t = Timer(f"for t in {query}: Solution().isUgly(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
