class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row, col = -1, 0
        N = len(s)
        cnt = 0
        conv = [["0"] * N for _ in range(numRows)]
        flag = True
        while cnt < N:
            if row <= 0:
                flag = True
            elif row == numRows - 1:
                flag = False

            if flag:
                row += 1
            else:
                row -= 1
                col += 1

            conv[row][col] = s[cnt]
            cnt += 1

        return "".join(["".join(r).replace("0", "") for r in conv])



s = Solution()
# print(s.convert("A", 1)) # A
print(s.convert("AB", 2)) # AB
# print(s.convert("PAYPALISHIRING", 2)) # PYAIHRNAPLSIIG
# print(s.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR
# print(s.convert("PAYPALISHIRING", 4)) # PINALSIGYAHRPI
# print(s.convert("PAYP,ALISHIR.pING", 5)) # PSGAIHNYLIIPARp,.
