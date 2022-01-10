from itertools import combinations

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 순서 인지 필요
        comb = list(combinations(nums, 2))
        print(f"comb: {comb}")
        i = 0
        ans = 0
        while i < len(comb)//2:
            s = min(comb[i]) + min(comb[-1-i])
            if ans < s: ans = s
            i += 1
        return ans


s = Solution()
#print(s.arrayPairSum([1,2,3,4]))
#print(s.arrayPairSum([1,4,3,2]))
print(s.arrayPairSum([6,2,6,5,1,2]))

