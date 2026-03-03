class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        log = []
        target, cnt = s[0], 1
        for ch in s[1:]:
            if target == ch:
                cnt += 1
            else:
                log.append(cnt)
                target = ch
                cnt = 1
        log.append(cnt)

        ans = 0
        for i in range(len(log)-1):
            ans += min(log[i], log[i+1])
        return ans


s = Solution()
# print(s.countBinarySubstrings("00110011"))  # 6
# print(s.countBinarySubstrings("000111"))    # 3
# print(s.countBinarySubstrings("10101"))     # 4
# print(s.countBinarySubstrings("1"))         # 0
# print(s.countBinarySubstrings("111"))       # 0
# print(s.countBinarySubstrings("00100"))     # 2
print(s.countBinarySubstrings("0010001"))   # 3
