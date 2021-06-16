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
        ret, power = 0, 24
        while n:
            ret += ((n & 0xff) * 0x0202020202 & 0x010884422010) % 1023 << power
            n = n >> 8
            power -= 8
        return ret

        # print(f"n & 0xff: {bin(n & 0xff)[2:]}")
        # print(f"* 0x0202020202: {bin((n & 0xff) * 0x0202020202)[2:]}")
        # print(f"int 0x0202020202: {int(0x0202020202)}")
        # print(f"& 0x010884422010: {bin((n & 0xff) * 0x0202020202 & 0x010884422010)[2:]}")
        # print(f"int & 0x010884422010: {(n & 0xff) * 0x0202020202 & 0x010884422010}")
        # print(f"%1023: {bin((n & 0xff) * 0x0202020202 & 0x010884422010 % 1023)[2:]}")
        # print(f"zfill: {bin((n & 0xff) * 0x0202020202 & 0x010884422010 % 1023)[2:].zfill(8)}")


s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))
# print(s.reverseBits(0b11111111111111111111111111111101))


if __name__ == '__main__':
    from timeit import Timer
    query = [0b00000010100101000001111010011100,
             0b11111111111111111111111111111101]
    t = Timer(f"for t in {query}: Solution().reverseBits(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
