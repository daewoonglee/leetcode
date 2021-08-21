class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        primes = [5, 3, 2]
        idx = 0
        while n:
            while n != 1:
                q, d = divmod(n, primes[idx])
                if d != 0:
                    break
                n = q
            idx += 1
            if idx > 2:
                break
        return True if n == 1 else False


s = Solution()
print(s.isUgly(10))
print(s.isUgly(60))
print(s.isUgly(61))
