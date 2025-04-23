class Solution:
    def scoreOfString(self, s: str) -> int:
        # ans = 0
        # for i in range(len(s)-1):
        #     ans += abs(ord(s[i])-ord(s[i+1]))
        # return ans

        return sum([abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)])


s = Solution()
print(s.scoreOfString("hello")) # 13
print(s.scoreOfString("zaz")) # 50
print(s.scoreOfString("aa")) # 50
