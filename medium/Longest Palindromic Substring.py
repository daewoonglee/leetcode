class Solution:
    def longestPalindrome(self, s: str) -> str:
        def set_palindrome(start, end, res):
            while start >= 0 and end < N and s[start] == s[end]:
                if (end - start + 1) > len(res):
                    res = s[start: end+1]
                start -= 1
                end += 1
            return res

        N = len(s)
        res = ""
        for i in range(N):
            res = set_palindrome(i, i, res)
            res = set_palindrome(i, i+1, res)
        return res


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
