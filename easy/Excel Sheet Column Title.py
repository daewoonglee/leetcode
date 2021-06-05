class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        word = {i+1: c for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        ans = []
        while columnNumber > 26:
            columnNumber, d = divmod(columnNumber, 26)
            if d == 0:
                columnNumber -= 1
                d = 26
            ans.append(d)
        if columnNumber != 0:
            ans.append(columnNumber)
        # print(ans)
        return "".join([word[i] for i in ans[::-1]])


s = Solution()
# print(s.convertToTitle(1))          # A
# print(s.convertToTitle(25))         # Y
# print(s.convertToTitle(26))         # Z
# print(s.convertToTitle(27))         # AA
# print(s.convertToTitle(28))         # AB
# print(s.convertToTitle(52))         # AZ
# print(s.convertToTitle(53))         # BA
# print(s.convertToTitle(78))         # BZ
# print(s.convertToTitle(701))        # ZY
print(s.convertToTitle(703))        # AAA
print(s.convertToTitle(2147483647)) # FXSHRXW
