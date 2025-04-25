from itertools import combinations


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        ans = sum(nums)
        for r in range(2, len(nums)+1):
            for c in combinations(nums, r):
                a = c[0]
                for i in range(1, len(c)):
                    a = a ^ c[i]
                ans += a
        return ans


s = Solution()
# print(s.subsetXORSum([1,3])) # 6
# print(s.subsetXORSum([5,1,6])) # 28
print(s.subsetXORSum([3,4,5,6,7,8])) # 480
