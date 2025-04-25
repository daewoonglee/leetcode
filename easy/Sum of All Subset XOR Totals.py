class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        ans = 0
        for n in nums:
            ans |= n
        return ans * 2**(len(nums)-1)


s = Solution()
# print(s.subsetXORSum([1,3])) # 6
print(s.subsetXORSum([5,1,6])) # 28
# print(s.subsetXORSum([3,4,5,6,7,8])) # 480
