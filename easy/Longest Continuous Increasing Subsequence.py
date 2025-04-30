class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        # ans = 1
        # temp = 1
        # for i in range(1, len(nums)):
        #     if nums[i-1] < nums[i]:
        #         temp += 1
        #     else:
        #         ans = ans if ans > temp else temp
        #         temp = 1
        # return ans if ans > temp else temp

        # dp version
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + dp[i]
        return max(dp)


s = Solution()
# print(s.findLengthOfLCIS([1,3,5,4,7])) # 3
# print(s.findLengthOfLCIS([2,2,2,2,2])) # 1
# print(s.findLengthOfLCIS([2])) # 1
# print(s.findLengthOfLCIS([5,4,3,2,1])) # 1
print(s.findLengthOfLCIS([-3,-2,-1,0,-1,-2])) # 4