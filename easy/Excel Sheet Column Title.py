class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # 0.401345426
        # word = {i+1: c for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        # ans = []
        # while columnNumber > 26:
        #     columnNumber, d = divmod(columnNumber, 26)
        #     if d == 0:
        #         columnNumber -= 1
        #         d = 26
        #     ans.append(d)
        # if columnNumber != 0:
        #     ans.append(columnNumber)
        # return "".join([word[i] for i in ans[::-1]])

        # code refactoring - 0.152382443
        # word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # ans = []
        # while columnNumber > 26:
        #     columnNumber, d = divmod(columnNumber, 26)
        #     if d == 0:
        #         columnNumber -= 1
        #         d = 26
        #     ans.append(d)
        # ans.append(columnNumber)
        # return "".join([word[i-1] for i in ans])[::-1]

        # code refactoring (R) - 0.137454049
        res = []
        while columnNumber:
            columnNumber -= 1
            columnNumber, d = divmod(columnNumber, 26)
            res.append(chr(d + ord('A')))
        return ''.join(res)[::-1]


s = Solution()
# print(s.convertToTitle(1))          # A
# print(s.convertToTitle(25))         # Y
# print(s.convertToTitle(26))         # Z
# print(s.convertToTitle(27))         # AA
# print(s.convertToTitle(28))         # AB
print(s.convertToTitle(52))         # AZ
# print(s.convertToTitle(53))         # BA
# print(s.convertToTitle(78))         # BZ
# print(s.convertToTitle(701))        # ZY
# print(s.convertToTitle(703))        # AAA
# print(s.convertToTitle(2147483647)) # FXSHRXW


if __name__ == '__main__':
    from timeit import Timer
    query = [1, 25, 26, 27, 28, 52, 53, 78, 701, 703, 2147483647]
    t = Timer(f"for t in {query}: Solution().convertToTitle(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
