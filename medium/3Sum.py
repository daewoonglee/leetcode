class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        nums.sort()
        ans = []
        for i, target in enumerate(nums):
            if target > 0: break
            if i > 0 and target == nums[i - 1]: continue

            L, R = i + 1, N - 1
            while L < R:
                total = target + nums[L] + nums[R]
                if total == 0:
                    ans.append([target, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                elif total > 0:
                    R -= 1
                else:
                    L += 1
        return ans


s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# print(s.threeSum([0,1,1])) # []
# print(s.threeSum([0,0,0])) # [[0,0,0]]
# print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,7])) # [[-4, -3, 7], [-3, 1, 2], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
# print(s.threeSum([-4,-3,-2,-1,-1,0,1,2,7])) # [[-4, -3, 7], [-3, 1, 2], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
# print(s.threeSum([-4,-3,0,2,2,2,2,7])) # [[-4, -3, 7], [-4, 2, 2]]
print(s.threeSum([-1,0,0,0,0,1,1,1,1])) # [[-1, 0, 1], [0, 0, 0]]
