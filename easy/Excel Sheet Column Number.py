class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # 0.120459024
        # alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # ans = alpha.index(columnTitle[0])+1
        # for ch in columnTitle[1:]:
        #     ans *= 26
        #     ans += alpha.index(ch)+1
        # return ans

        # code refactoring - 0.093942284
        # alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # ans = 0
        # for ch in columnTitle:
        #     ans = ans * 26 + alpha.index(ch) + 1
        # return ans

        # code refactoring (R) 01 - 0.092704572
        # ans = 0
        # for ch in columnTitle:
        #     ans = ans * 26 + ord(ch)-ord('A') + 1
        # return ans

        # code refactoring (R) 02 - 0.148181161
        # ans = 0
        # for i, ch in enumerate(columnTitle[::-1]):
        #     ans += (ord(ch) - 64) * pow(26, i)
        # return ans

        # code refactoring (R) 03 - 0.14501782600000002
        N = len(columnTitle)
        ans = 0
        for i in range(N):
            ans = ans + 26**i * (ord(columnTitle[N-i-1])-64)
        return ans


s = Solution()
# print(s.titleToNumber("A"))     # 1
# print(s.titleToNumber("Z"))     # 26
# print(s.titleToNumber("AA"))    # 27
# print(s.titleToNumber("AZ"))    # 52
# print(s.titleToNumber("BA"))    # 53
# print(s.titleToNumber("ZY"))    # 701
# print(s.titleToNumber("ZZ"))    # 702
# print(s.titleToNumber("AAA"))   # 703
# print(s.titleToNumber("XFC"))   # 16383
print(s.titleToNumber("FXSHRXW"))   # 2147483647


if __name__ == '__main__':
    from timeit import Timer
    query = ["A", "Z", "AA", "AZ", "BA", "ZY", "ZZ", "AAA", "XFC", "FXSHRXW"]
    t = Timer(f"for t in {query}: Solution().titleToNumber(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
