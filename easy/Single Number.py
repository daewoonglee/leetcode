class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]


s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([1]))
print(s.singleNumber([4, 1, 2, 1, 2]))
