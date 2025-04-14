from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        ans = 0
        c_dict = Counter(nums)
        for k, v in c_dict.items():
            if k+1 in c_dict:
                ans = ans if ans > c_dict[k+1]+v else c_dict[k+1]+v
        return ans


s = Solution()
print(s.findLHS([1,2,2,2,3,3,5,7])) # 5
print(s.findLHS([0,0,0,0,0,1,2,2,2,3,3,5,7])) # 6
print(s.findLHS([1,2,3,4])) # 2
print(s.findLHS([1,1,1,1])) # 0
print(s.findLHS([-1,-2,1,-2])) # 3
