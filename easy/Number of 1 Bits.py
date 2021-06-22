class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0.064489119
        # cnt = 0
        # while n:
        #     if n & 1:
        #         cnt += 1
        #     n >>= 1
        # return cnt

        # code refactoring (R) - 0.047009155999999996
        cnt = 0
        while n:
            # print(f"n: {n}, n-1: {n-1}, &: {n&n-1}")
            cnt += 1
            n &= (n-1)
        return cnt


s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b00000000000000000000000010000000))
print(s.hammingWeight(0b11111111111111111111111111111101))
print(s.hammingWeight(0b00000000000000000000000000000000))


if __name__ == '__main__':
    from timeit import Timer
    query = [0b00000000000000000000000000001011,
             0b00000000000000000000000010000000,
             0b11111111111111111111111111111101,
             0b00000000000000000000000000000000]
    t = Timer(f"for t in {query}: Solution().hammingWeight(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
