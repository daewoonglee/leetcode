class Solution:
    def longestPalindrome(self, s: str) -> str:
        ps = "@" + "#".join(s) + "$"
        P = [0] * len(ps)
        R, C = 0, 0
        for i in range(1, len(ps)-1):
            if i < R:
                mirror = 2*C-i
                P[i] = min(R-i, P[mirror])
            while ps[i-P[i]-1] == ps[i+P[i]+1]:
                P[i] += 1

            if i+P[i] > R:
                C = i
                R = i+P[i]

        ans = ""
        longest_radius = max(P)
        for center, radius in enumerate(P):
            if radius == longest_radius:
                plus = 1 if center % 2 != 0 or ps[center] == "#" else 0
                N = len(ans) if ans and ans[0] != "#" else len(ans)-2
                ans = ps[center-radius: center+radius+plus] if N < 2*radius+plus else ans
        return ans.replace("#", "") if len(ans) else s[0]


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
