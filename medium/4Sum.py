class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]: continue
            for j in range(i+1, N):
                if j > i+1 and nums[j-1] == nums[j]: continue
                L, R = j+1, N-1
                while L < R:
                    total = n + nums[L] + nums[R] + nums[j]
                    if total == target:
                        ans.append([n, nums[L], nums[R], nums[j]])
                        L += 1
                        R -= 1
                        while L < R and nums[L-1] == nums[L]:
                            L += 1
                    elif total > target:
                        R -= 1
                    else:
                        L += 1
        return ans


s = Solution()
# print(s.fourSum([-2,-1,0,0,1,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum([2,2,2,2,2], 8)) # [[2,2,2,2]]
# print(s.fourSum([2], 8)) # [[]]
