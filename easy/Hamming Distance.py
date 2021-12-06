class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # version1
        # return bin(x ^ y).count("1")

        # version2
        def conv_bin(n):
            arr = []
            while n:
                d = n % 2
                n //= 2
                arr.append(d)
            return "".join(list(map(str, arr))[::-1])

        bin_x = conv_bin(x)
        bin_y = conv_bin(y)
        if len(bin_x) < len(bin_y): bin_x = bin_x.zfill(len(bin_y))
        else: bin_y = bin_y.zfill(len(bin_x))

        ans = 0
        for xn, yn in zip(bin_x, bin_y):
            if int(xn) ^ int(yn): ans += 1
        return ans

s = Solution()
print(s.hammingDistance(1, 4))
print(s.hammingDistance(1, 3))



