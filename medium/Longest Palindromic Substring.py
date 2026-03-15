class Solution:
    def longestPalindrome(self, s: str) -> str:
        def set_palindrome(start: int, end: int) -> str:
            while start >= 0 and end < N and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1: end]

        N = len(s)
        ans = ""
        for i in range(N):
            odd = set_palindrome(i, i)
            even = set_palindrome(i, i + 1)
            ans = max(ans, odd, even, key=len)
        return ans


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
print(s.longestPalindrome("abcdefghihhhihhhhijklmopqrtuvwxyz1234567890000000")) # aabbbbbbaa
