from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # UD = 0
        # LR = 0
        # for m in moves:
        #     if m == "R":
        #         LR += 1
        #     elif m == "L":
        #         LR -= 1
        #     elif m == "U":
        #         UD += 1
        #     else:
        #         UD -= 1
        # return True if UD == 0 and LR == 0 else False

        c = Counter(moves)
        return True if c["U"] - c["D"] == 0 and c["L"] - c["R"] == 0 else False


s = Solution()
print(s.judgeCircle("UD")) # true
print(s.judgeCircle("LL")) # false
print(s.judgeCircle("L")) # false
print(s.judgeCircle("UUUUUDDDDDRD")) # false
