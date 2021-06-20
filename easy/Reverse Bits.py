class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 0.023247772
        # bn = bin(n)
        # bn = "0" * (34-len(bn)) + bn[2:]
        # return int(bn[::-1], 2)

        # code refactoring (R) 01 - 0.12206612800000001
        # p = 31
        # ans = 0
        # while n:
        #     ans += (n & 1) << p
        #     p -= 1
        #     n = n >> 1
        # return ans

        # code refactoring (R) 02 - 0.039573159000000004
        # ret, power = 0, 24
        # while n:
        #     ret += ((n & 0xff) * 0x0202020202 & 0x010884422010) % 1023 << power
        #     n = n >> 8
        #     power -= 8
        # return ret

        # n_and_ff = (n & 0xff)
        # n_and_ff_mul_02 = n_and_ff * n_and_ff
        # n_and_ff_mul_02_and_010 = n_and_ff_mul_02 & 0x010884422010
        # print(f"n: {bin(n)}")                                               # 00000010 10010100 00011110 10011100
        # print(f"0xff, 10base: {0xff}, 2base: {bin(0xff)}")                  # 00000000 00000000 00000000 11111111
        # print(f"n & 0xff: {n_and_ff}")                                      # 00000000 00000000 00000000 10011100
        #
        # print(f"n & 0xff: {n_and_ff}")                                      # 00000000 00000000 00000000 10011100
        # print(f"0x0202020202 2base: {bin(0x0202020202)}")                   # 00000010 00000010 00000010 00000010 00000010
        # print(f"* 0x0202020202: {bin(n_and_ff_mul_02)}")                    # 00000000 00000000 00000000 01011111 00010000
        #
        # print(f"* 0x0202020202: {bin(n_and_ff_mul_02)}")                    # 00000000 00000000 00000000 00000000 01011111 00010000
        # print(f"0x010884422010 2base: {bin(0x010884422010)}")               # 00000001 00001000 10000100 01000010 00100000 00010000
        # print(f"& 0x010884422010: {bin(n_and_ff_mul_02_and_010)[2:]}")      #                                              00010000
        #
        # print(f"%1023: {bin(n_and_ff_mul_02_and_010 % 1023)}")              # 10000
        # print(f"zfill: {bin(n_and_ff_mul_02_and_010 % 1023)[2:].zfill(8)}") # 00011000

        # code refactoring (R) 03 - 0.023379218000000004
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

        # print(f"n: {bin(n)}")                       #                   00000010 10010100 00011110 10011100)
        # print(f"n >> 16: {bin(n >> 16)}")           # 00000000 00000000 00000000 00000000 00000010 10010100
        # print(f"n << 16: {bin(n << 16)}")           # 00000010 10010100 00011110 10011100 00000000 00000000
        # print(f"| : {bin((n >> 16) | (n << 16))}")  # 00000010 10010100 00011110 10011100 00000010 10010100
        #
        # print(bin(0xf0f0f0f0)) # 11110000 11110000 11110000 11110000 (0 and 1 appear alternately every four digits)
        # print(bin(0x0f0f0f0f)) # 00001111 00001111 00001111 00001111 (1 and 0 appear alternately every four digits)
        # print(bin(0xcccccccc)) # 11001100 11001100 11001100 11001100 (0 and 1 appear alternately every two digits)
        # print(bin(0x33333333)) # 00110011 00110011 00110011 00110011 (1 and 0 alternate every two digits)
        # print(bin(0x55555555)) # 01010101 01010101 01010101 01010101 (even bits are 0, odd bits are 1)
        # print(bin(0xaaaaaaaa)) # 10101010 10101010 10101010 10101010 (even bit is 1, odd bit is 0)


s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))
# print(s.reverseBits(0b11111111111111111111111111111101))


if __name__ == '__main__':
    from timeit import Timer
    query = [0b00000010100101000001111010011100,
             0b11111111111111111111111111111101]
    t = Timer(f"for t in {query}: Solution().reverseBits(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
