class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [bin(i)[2:].count("1") for i in range(n+1)]


s = Solution()
print(s.countBits(0))
print(s.countBits(1))
print(s.countBits(2))
print(s.countBits(3))
print(s.countBits(4))
print(s.countBits(5))
print(s.countBits(6))

