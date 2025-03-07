class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        N = len(sequence)
        W = len(word)
        dp = [0] * N
        for i in range(N):
            if sequence[i: i+W] == word:
                dp[i] = dp[i-W] + 1
        return max(dp)


s = Solution()
# print(s.maxRepeating("ababc", "ab")) # 2
# print(s.maxRepeating("ababc", "ba")) # 1
# print(s.maxRepeating("ababc", "ac")) # 0
# print(s.maxRepeating("aaaaaa", "aa")) # 3
print(s.maxRepeating("aaaaa", "aaa")) # 1
print(s.maxRepeating("aaabaaaabaa", "aa")) # 2
