class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]


s = Solution()
print(s.tribonacci(0)) # 0
print(s.tribonacci(1)) # 1
print(s.tribonacci(2)) # 1
print(s.tribonacci(3)) # 2
print(s.tribonacci(4)) # 4
print(s.tribonacci(25)) # 4
