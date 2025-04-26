class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[n] for n in nums]


s = Solution()
print(s.buildArray([0,2,1,5,3,4])) # [0,1,2,4,5,3]
print(s.buildArray([5,0,1,2,3,4])) # [4,5,0,1,2,3]
