from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ans = 0
        # substr = deque()
        # for ch in s:
        #     while ch in substr:
        #         substr.popleft()
        #     substr.append(ch)
        #     ans = ans if ans > len(substr) else len(substr)
        # return ans

        last = {}
        cur_idx = -1
        ans = 0
        for i, ch in enumerate(s):
            if ch in last:
                cur_idx = last[ch] if last[ch] > cur_idx else cur_idx
            last[ch] = i
            ans = ans if ans > i - cur_idx else i - cur_idx
        return ans


s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb"))       # 3
# print(s.lengthOfLongestSubstring("bbbbb"))          # 1
# print(s.lengthOfLongestSubstring("pwwkew"))         # 3
# print(s.lengthOfLongestSubstring("44454321"))       # 5
print(s.lengthOfLongestSubstring("1234543210"))     # 6
