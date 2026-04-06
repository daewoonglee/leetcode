class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        N = len(nums)-1
        ans = set()
        for i, n in enumerate(nums):
            for j in range(N, i, -1):
                L, R = i+1, j-1
                while L < R:
                    total = n + nums[L] + nums[R] + nums[j]
                    if total == target:
                        ans.add((n, nums[L], nums[R], nums[j]))
                        L += 1
                        R -= 1
                    elif total > target:
                        R -= 1
                    else:
                        L += 1
        return [list(t) for t in ans]


s = Solution()
# print(s.fourSum([-2,-1,0,0,1,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# print(s.fourSum([2,2,2,2,2], 8)) # [[2,2,2,2]]
print(s.fourSum([2], 8)) # [[]]
