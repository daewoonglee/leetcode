from collections import defaultdict


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        log = defaultdict(int)
        for k in range(1, N):
            for i in range(k+1, N): # a+b = d-c
                ans += log[nums[i] - nums[k]]
            for i in range(k):
                log[nums[i] + nums[k]] += 1
        return ans


s = Solution()
# print(s.countQuadruplets([1,2,3,6])) # 1
# print(s.countQuadruplets([3,3,6,4,5])) # 0
# print(s.countQuadruplets([1,1,1,3,5])) # 4
# print(s.countQuadruplets([1,1,3,1,5])) # 3
print(s.countQuadruplets([1,1,3,1,5,5])) # 6
