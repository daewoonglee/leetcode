class Solution:
    def countVowelStrings(self, n: int) -> int:
        def counting(idx, depth):
            if depth+1 < n:
                c = 0
                for j, v in enumerate(vowel[idx:]):
                    c += counting(idx+j, depth=depth+1)
            else:
                c = len(vowel[idx:])
            return c

        vowel = ["a", "e", "i", "o", "u"]
        return counting(0, 0)


s = Solution()
print(s.countVowelStrings(1)) # 5
print(s.countVowelStrings(2)) # 15    10
print(s.countVowelStrings(3)) # 35    20
print(s.countVowelStrings(4)) # 70    35
print(s.countVowelStrings(5)) # 126   56
