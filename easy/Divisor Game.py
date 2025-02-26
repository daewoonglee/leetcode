class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


s = Solution()
# print(s.divisorGame(1)) # False
# print(s.divisorGame(2)) # True
# print(s.divisorGame(4)) # True
print(s.divisorGame(7)) # False
