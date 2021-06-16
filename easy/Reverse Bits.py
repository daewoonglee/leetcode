class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bn = bin(n)
        bn = "0" * (34-len(bn)) + bn[2:]
        return int(bn[::-1], 2)


s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))
print(s.reverseBits(0b11111111111111111111111111111101))
