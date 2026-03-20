class Solution:
    def longestPalindrome(self, s: str) -> str:
        ps = "@" + "#".join(s) + "$"
        P = [0] * len(ps)
        R, C = 0, 0
        best_center, best_len = 0, 0

        for i in range(1, len(ps)-1):
            if i < R:
                P[i] = min(R-i, P[2*C-i])

            while ps[i-P[i]-1] == ps[i+P[i]+1]:
                P[i] += 1

            if i+P[i] > R:
                C = i
                R = i+P[i]

            if P[i] >= best_len:
                actual = len(ps[i - P[i]: i + P[i] + 1].replace("#", ""))
                if actual > best_len:
                    best_len, best_center = actual, i

        radius = P[best_center]
        return ps[best_center - radius: best_center + radius + 1].replace("#", "") if radius > 0 else s[0]


s = Solution()
# print(s.longestPalindrome("babad")) # bab or aba
# print(s.longestPalindrome("cbbd")) # bb
# print(s.longestPalindrome("abc")) # a or b or c
# print(s.longestPalindrome("aaaaaa")) # aaaaaa
# print(s.longestPalindrome("aabbbbbbaaaaaab")) # aabbbbbbaa
print(s.longestPalindrome("aabbbbbbaaab")) # aabbbbbbaa
# print(s.longestPalindrome("aabbbbbbaaabbbbbb")) # bbbbbbaaabbbbbb
# print(s.longestPalindrome("abbcccba")) # bcccb
# print(s.longestPalindrome("a")) # a
print(s.longestPalindrome("abcdefghihhhihhhhijklmopqrtuvwxyz1234567890000000")) # hhhihhh
