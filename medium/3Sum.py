class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i, target in enumerate(nums):
            dp = dict()
            for j in range(i+1, len(nums)):
                n = -(nums[j] + target)
                if n in dp:
                    ans.append((target, nums[j], n))
                dp[nums[j]] = n
        return [list(t) for t in set(ans)]


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# print(s.threeSum([0,1,1])) # []
# print(s.threeSum([0,0,0])) # [[0,0,0]]
