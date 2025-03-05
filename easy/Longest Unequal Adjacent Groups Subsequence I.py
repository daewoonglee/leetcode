class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        ans = [words[0]]
        pre_g = groups[0]
        for w, g in zip(words[1:], groups[1:]):
            if pre_g != g:
                ans.append(w)
            pre_g = g
        return ans


s = Solution()
print(s.getLongestSubsequence(["e","a","b"], [0,0,1])) # e b or a b
print(s.getLongestSubsequence(["a","b","c","d"], [1,0,1,1])) # a b c or a b d
print(s.getLongestSubsequence(["a","b","c","d","e"], [0,0,0,1,0])) # a b c or a b d
