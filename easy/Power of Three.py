class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = 1
        while t <= n:
            if n == t:
                return True
            t *= 3
        return False
            

s = Solution()
print(s.isPowerOfThree(27))
print(s.isPowerOfThree(0))
print(s.isPowerOfThree(45))
 
