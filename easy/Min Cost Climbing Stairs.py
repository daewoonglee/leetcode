class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        N = len(cost)
        if N == 2:
            return min(cost)
        elif N == 3:
            return min(cost[0]+cost[2], cost[1])

        climbing = [float('inf') for _ in range(N)]
        climbing[0] = cost[0]
        climbing[1] = cost[1]
        idx = 0
        while idx < N-2:
            climbing[idx+1] = min(climbing[idx+1], climbing[idx] + cost[idx+1]) # step1
            climbing[idx+2] = min(climbing[idx+2], climbing[idx] + cost[idx+2])  # step2
            idx += 1

        # inf 경우 X
        return min(climbing[-1], climbing[-2])


s = Solution()
# print(s.minCostClimbingStairs([125, 20])) # 20
# print(s.minCostClimbingStairs([10, 15, 20])) # 15
# print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) # 6
# print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,10])) # 5
# print(s.minCostClimbingStairs([0, 1, 1, 0])) # 1
# print(s.minCostClimbingStairs([0, 1, 20, 3, 40, 5, 4, 3, 2, 1, 0])) # 12
print(s.minCostClimbingStairs([100,400,200,600,800,800,800]))
