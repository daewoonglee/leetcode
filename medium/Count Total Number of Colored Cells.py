class Solution:
    def coloredCells(self, n: int) -> int:
        # dp version
        # dp = [1]*(n+1)
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + 4*(i-1)
        # return dp[-1]

        # ans = 1
        # for i in range(2, n+1):
        #     ans += 4*(i-1)
        # return ans

        # code refactoring
        return n*n*2 - 2*n+1


s = Solution()
print(s.coloredCells(1)) # 1    +0  4*(n-1)
print(s.coloredCells(2)) # 5    +4
print(s.coloredCells(3)) # 13   +8
print(s.coloredCells(4)) # 25   +12
print(s.coloredCells(5)) # 41   +16
print(s.coloredCells(6)) # 61   +20
