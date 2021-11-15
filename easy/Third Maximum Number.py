class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(set(nums), reverse=True)
        return sort_nums[2] if len(sort_nums) > 2 else sort_nums[0]


s = Solution()
print(s.thirdMax([1,1,3,2,0]))
print(s.thirdMax([1,1,1,1,1,1,1,1,1,3]))
 
