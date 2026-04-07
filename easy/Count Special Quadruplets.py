from collections import Counter


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        log = Counter()
        log[nums[-1]] = 1
        for k in range(N-2, 1, -1):
            for i in range(k-1):
                for j in range(i+1, k):
                    total = nums[i] + nums[j] + nums[k]
                    if total in log:
                        ans += log[total]
            log[nums[k]] += 1
        return ans



s = Solution()
# print(s.countQuadruplets([1,2,3,6])) # 1
# print(s.countQuadruplets([3,3,6,4,5])) # 0
# print(s.countQuadruplets([1,1,1,3,5])) # 4
# print(s.countQuadruplets([1,1,3,1,5])) # 3
print(s.countQuadruplets([1,1,3,1,5,5])) # 6
'''
[1,1,1,3,5]
0 1 3 4 -> 1 1 3 5
0 2 3 4 -> 1 1 3 5
1 2 3 4 -> 1 1 3 5
0 1 2 3 -> 1 1 1 3


[1,1,3,1,5]
0 1 2 4 -> 1 1 3 5
0 2 3 4 -> 1 3 1 5
1 2 3 4 -> 1 3 1 5
'''
# print(s.countQuadruplets([1,1,1,1,3])) # 4
