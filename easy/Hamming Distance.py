class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # version1 - 0.024727134965360165
        #return bin(x ^ y).count("1")

        # version2 - 0.4886663295328617
        #def conv_bin(n):
        #    arr = []
        #    while n:
        #        d = n % 2
        #        n //= 2
        #        arr.append(d)
        #    return "".join(list(map(str, arr))[::-1])
        #
        #bin_x = conv_bin(x)
        #bin_y = conv_bin(y)
        #if len(bin_x) < len(bin_y): bin_x = bin_x.zfill(len(bin_y))
        #else: bin_y = bin_y.zfill(len(bin_x))
        #
        #diff = ord("1") - ord("0")        
        #ans = 0
        #for xn, yn in zip(bin_x, bin_y):
        #    #if int(xn) ^ int(yn): ans += 1
        #
        #    # code refactoring - 0.4002802334725857
        #    if abs(ord(xn)-ord(yn)) == diff: ans += 1
        #return ans

        # code refactoring (R) - 0.16764191817492247
        ans = 0
        mask = x ^ y
        limit = len(bin(mask)) - 2
        bit = 1
        for idx in range(limit):
            if mask & bit > 0: ans += 1
            bit <<= 1
        return ans


s = Solution()
print(s.hammingDistance(1, 4))
print(s.hammingDistance(1, 3))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1,4], [1,3], [10000, 11123], [123456789, 987654321], [0, 0]]
    t = Timer(f"for t in {query}: Solution().hammingDistance(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

