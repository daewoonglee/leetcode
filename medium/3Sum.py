class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        nums.sort()
        ans = set()
        is_searched = {}
        for i, target in enumerate(nums):
            if target > 0: break

            if target in is_searched: continue
            is_searched[target] = True

            dp = {}
            for j in range(i+1, N):
                n = -(nums[j] + target)
                if n in dp:
                    ans.add((target, nums[j], n))
                dp[nums[j]] = n
        return [list(t) for t in ans]


s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# print(s.threeSum([0,1,1])) # []
# print(s.threeSum([0,0,0])) # [[0,0,0]]
print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,7])) # [[-1,-1,2],[-1,0,1]]
