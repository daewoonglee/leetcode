class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num ** 0.5) % 2 in [0, 1]


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
print(s.isPerfectSquare(1))
print(s.isPerfectSquare(2))
print(s.isPerfectSquare(3))
print(s.isPerfectSquare(9))

