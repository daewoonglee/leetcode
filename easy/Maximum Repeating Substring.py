class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        N = len(word)
        for i in range(len(sequence) - N + 1):
            if sequence[i: i+N] == word:
                tmp_ans = 1
                j = 1
                while 1:
                    if sequence[i+N*j: i+N*(j+1)] == word:
                        tmp_ans += 1
                    else: break
                    j += 1
                if ans < tmp_ans:
                    ans = tmp_ans
        return ans


s = Solution()
# print(s.maxRepeating("ababc", "ab")) # 2
# print(s.maxRepeating("ababc", "ba")) # 1
# print(s.maxRepeating("ababc", "ac")) # 0
# print(s.maxRepeating("aaaaaa", "aa")) # 3
print(s.maxRepeating("aaaaa", "aaa")) # 1
print(s.maxRepeating("aaabaaaabaa", "aa")) # 2
