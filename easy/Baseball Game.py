class Solution:
    def calPoints(self, operations: list[str]) -> int:
        ans = []
        for opt in operations:
            if opt == "C":
                ans.pop()
            elif opt == "D":
                ans.append(ans[-1]*2)
            elif opt == "+":
                ans.append(ans[-2]+ans[-1])
            else:
                ans.append(int(opt))
        return sum(ans)


s = Solution()
print(s.calPoints(["5","2","C","D","+"])) # 30
print(s.calPoints(["5","-2","4","C","D","9","+","+"])) # 27
print(s.calPoints(["1","C"])) # 0
