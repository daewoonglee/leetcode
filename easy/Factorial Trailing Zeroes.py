class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n-1)
        fn = str(factorial(n))
        print(f"fn: {fn}")
        cnt = 0
        N = len(fn)
        for i in range(N):
            if fn[N-1-i] != "0":
                break
            cnt += 1
        return cnt


s = Solution()
print(s.trailingZeroes(3))
print(s.trailingZeroes(5))
print(s.trailingZeroes(7))
