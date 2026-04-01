from itertools import combinations
from collections import Counter


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        filtered_num = [k for k, v in Counter(nums).items() for _ in range(min(v, 3))]
        ans = []
        for c in combinations(filtered_num, 3):
            c = sorted(list(c))
            if sum(c) == 0:
                ans.append(c)
        return [list(t) for t in set(map(tuple, ans))]


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# print(s.threeSum([0,1,1])) # []
# print(s.threeSum([0,0,0])) # [[0,0,0]]
