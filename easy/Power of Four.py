class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1
        while x <= n:
            if x == n:
                return True
            x *= 4
        return False


s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(0))

