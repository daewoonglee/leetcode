class Solution:
    def divisorGame(self, n: int) -> bool:
        game = [False for _ in range(n+1)]
        for num in range(n+1):
            for x in range(1, num//2+1):
                if num % x == 0 and not game[num-x]:
                    game[num] = True
                    break
        return game[n]


s = Solution()
# print(s.divisorGame(1)) # False
# print(s.divisorGame(2)) # True
# print(s.divisorGame(4)) # True
print(s.divisorGame(7)) # False
