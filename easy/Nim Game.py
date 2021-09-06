class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


s = Solution()
print(s.canWinNim(1))
print(s.canWinNim(1))   # T
print(s.canWinNim(2))   # T
print(s.canWinNim(3))   # T
print(s.canWinNim(4))   # F
print(s.canWinNim(5))   # T
print(s.canWinNim(6))   # T
print(s.canWinNim(7))   # T
print(s.canWinNim(8))   # F
print(s.canWinNim(9))   # T

