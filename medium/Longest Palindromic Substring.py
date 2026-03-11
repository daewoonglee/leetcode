class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_palindrome(start):
            for end in range(N-1, start, -1):
                if lower_s[start] == lower_s[end]:
                    left, right = start+1, end-1
                    while left < right:
                        if lower_s[left] == lower_s[right]:
                            left += 1
                            right -= 1
                        else:
                            break
                    else:
                        return s[start: end+1]
            return ""

        N = len(s)
        lower_s = s.lower()
        ans = s[0]
        for i in range(N):
            sub_palindrome = get_palindrome(i)
            print(f"i: {i}, sub: {sub_palindrome}")
            ans = ans if len(ans) > len(sub_palindrome) else sub_palindrome
        return ans


s = Solution()
# print(s.longestPalindrome("babad")) # bab or aba
# print(s.longestPalindrome("cbbd")) # bb
# print(s.longestPalindrome("abc")) # a or b or c
# print(s.longestPalindrome("aaaaaa")) # aaaaaa
# print(s.longestPalindrome("aabbbbbbaaaaaab")) # aabbbbbbaa
# print(s.longestPalindrome("aabbbbbbaaabbbbbb")) # bbbbbbaaabbbbbb
print(s.longestPalindrome("abbcccba")) # bcccb
print(s.longestPalindrome("a")) # a
