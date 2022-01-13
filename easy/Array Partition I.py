from itertools import combinations

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


s = Solution()
#print(s.arrayPairSum([1,2,3,4]))
#print(s.arrayPairSum([1,4,3,2]))
print(s.arrayPairSum([6,2,6,5,1,2]))

