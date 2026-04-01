from itertools import combinations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        for c in combinations(nums, 3):
            c = sorted(list(c))
            if sum(c) == 0 and c not in ans:
                ans.append(c)
        return ans


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# print(s.threeSum([0,1,1])) # []
# print(s.threeSum([0,0,0])) # [[0,0,0]]
