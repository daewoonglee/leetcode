class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = alpha.index(columnTitle[0])+1
        for ch in columnTitle[1:]:
            ans *= 26
            ans += alpha.index(ch)+1
        return ans


s = Solution()
print(s.titleToNumber("A"))     # 1
print(s.titleToNumber("Z"))     # 26
print(s.titleToNumber("AA"))    # 27
print(s.titleToNumber("AZ"))    # 52
print(s.titleToNumber("BA"))    # 53
print(s.titleToNumber("ZY"))    # 701
print(s.titleToNumber("ZZ"))    # 702
print(s.titleToNumber("AAA"))   # 703
print(s.titleToNumber("XFC"))   # 16383
print(s.titleToNumber("FXSHRXW"))   # 2147483647
