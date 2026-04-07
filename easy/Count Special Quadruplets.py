class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        # nums.sort()
        N = len(nums)
        ans = 0
        for i in range(N-3):
            for j in range(i+1, N-2):
                for z in range(j+1, N-1):
                    for k in range(z+1, N):
                        if nums[i] + nums[j] + nums[z] == nums[k]:
                            ans += 1
                            print(i, j, z, k)
        return ans


s = Solution()
# print(s.countQuadruplets([1,2,3,6])) # 1
# print(s.countQuadruplets([3,3,6,4,5])) # 0
# print(s.countQuadruplets([1,1,1,3,5])) # 4
# print(s.countQuadruplets([1,1,3,1,5])) # 3
print(s.countQuadruplets([1,1,1,1,3])) # 4
