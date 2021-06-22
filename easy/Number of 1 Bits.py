class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n >>= 1
        return cnt


s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b00000000000000000000000010000000))
print(s.hammingWeight(0b11111111111111111111111111111101))
print(s.hammingWeight(0b00000000000000000000000000000000))
