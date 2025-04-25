class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(idx, xor):
            if idx == len(nums):
                return xor
            with_cur = dfs(idx+1, xor ^ nums[idx])
            without_cur = dfs(idx+1, xor)
            return with_cur + without_cur
        return dfs(0, 0)


s = Solution()
# print(s.subsetXORSum([1,3])) # 6
print(s.subsetXORSum([5,1,6])) # 28
# print(s.subsetXORSum([3,4,5,6,7,8])) # 480
