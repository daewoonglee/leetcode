class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = ["0" if int(bn) else "1" for bn in bin(num)[2:]]
        return int("".join(ans), 2)


s = Solution()
#print(s.findComplement(5))
print(s.findComplement(2))

