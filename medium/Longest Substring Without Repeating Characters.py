from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        substr = deque()
        for ch in s:
            if ch not in substr:
                substr.append(ch)
            else:
                ans = ans if ans > len(substr) else len(substr)
                while ch in substr:
                    substr.popleft()
                substr.append(ch)
        return ans if ans > len(substr) else len(substr)


s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb"))       # 3
# print(s.lengthOfLongestSubstring("bbbbb"))          # 1
# print(s.lengthOfLongestSubstring("pwwkew"))         # 3
# print(s.lengthOfLongestSubstring("44454321"))       # 5
print(s.lengthOfLongestSubstring("1234543210"))     # 6
