class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1]*5] + [[0]*5 for _ in range(n-1)]
        for i in range(1, n):
            for j in range(5):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return sum(dp[-1])


s = Solution()
print(s.countVowelStrings(1)) # 5
print(s.countVowelStrings(2)) # 15    10
print(s.countVowelStrings(3)) # 35    20
print(s.countVowelStrings(4)) # 70    35
print(s.countVowelStrings(5)) # 126   56
