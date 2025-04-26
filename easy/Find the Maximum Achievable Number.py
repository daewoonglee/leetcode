class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t*2


s = Solution()
# print(s.theMaximumAchievableX(4, 1)) # 6
# print(s.theMaximumAchievableX(3, 2)) # 7
print(s.theMaximumAchievableX(1, 50)) # 7
