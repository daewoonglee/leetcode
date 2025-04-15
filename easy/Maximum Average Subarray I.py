class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total_num = sum(nums[:k])
        ans = total_num
        for i in range(k, len(nums)):
            total_num += nums[i] - nums[i-k]
            ans = ans if total_num < ans else total_num
        return ans / k


s = Solution()
# print(s.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.7500
# print(s.findMaxAverage([5], 1)) # 5.0000
print(s.findMaxAverage([-1,-2,-3,-4,-5,-6,-7,-2,-1,0], 3)) # 5.0000
