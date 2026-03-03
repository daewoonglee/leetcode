class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        pre, cur = 0, 0
        target = s[0]
        for ch in s:
            if target == ch:
                cur += 1
            else:
                ans += min(pre, cur)
                target = ch
                pre = cur
                cur = 1
        return ans + min(pre, cur)


s = Solution()
# print(s.countBinarySubstrings("00110011"))  # 6
# print(s.countBinarySubstrings("000111"))    # 3
# print(s.countBinarySubstrings("10101"))     # 4
# print(s.countBinarySubstrings("1"))         # 0
# print(s.countBinarySubstrings("111"))       # 0
# print(s.countBinarySubstrings("00100"))     # 2
print(s.countBinarySubstrings("0010001"))   # 3
