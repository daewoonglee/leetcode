class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        ans = 0
        diff = 10**5
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
            L, R = i+1, N-1
            while L < R:
                total = n + nums[L] + nums[R]
                local_diff = abs(total-target)
                if local_diff < diff:
                    diff = local_diff
                    ans = total
                if total > target:
                    R -= 1
                else:
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        return ans


s = Solution()
# print(s.threeSumClosest([-4,-1,1,2], 1)) # 2
# print(s.threeSumClosest([0,0,0], 1)) # 0
# print(s.threeSumClosest([-1,0,1,2,3], 7)) # 6
# print(s.threeSumClosest([-10,10,1,2,4,5,-10], 10)) # 10
print(s.threeSumClosest([1000,1000,1000], -10000)) # 10
