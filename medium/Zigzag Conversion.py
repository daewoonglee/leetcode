class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        conv = [""] * numRows
        row, step = 0, 1
        for ch in s:
            if row <= 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            conv[row] += ch
            row += step
        return "".join(conv)


s = Solution()
# print(s.convert("A", 1)) # A
# print(s.convert("AB", 1)) # A
# print(s.convert("AB", 2)) # AB
# print(s.convert("PAYPALISHIRING", 2)) # PYAIHRNAPLSIIG
# print(s.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR
# print(s.convert("PAYPALISHIRING", 4)) # PINALSIGYAHRPI
print(s.convert("PAYP,ALISHIR.pING", 5)) # PSGAIHNYLIIPARp,.
