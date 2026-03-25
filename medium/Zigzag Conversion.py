class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = []
        step = (numRows-1)*2
        N = len(s)

        for row in range(numRows):
            i = row
            gap1 = step - row * 2
            gap2 = row * 2
            while i < N:
                ans.append(s[i])
                i += gap1 or step
                if gap2 and i < N:
                    ans.append(s[i])
                    i += gap2

        return "".join(ans)


s = Solution()
# print(s.convert("A", 1)) # A
# print(s.convert("AB", 1)) # A
# print(s.convert("AB", 2)) # AB
print(s.convert("PAYPALISHIRING", 2)) # PYAIHRNAPLSIIG
# print(s.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR
# print(s.convert("PAYPALISHIRING", 4)) # PINALSIGYAHRPI
# print(s.convert("PAYP,ALISHIR.pING", 5)) # PSGAIHNYLIIPARp,.
