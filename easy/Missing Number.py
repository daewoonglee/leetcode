class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        nums.sort()
        for i in range(N):
            if i != nums[i]:
                return i
        return N


s = Solution()
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber([0, 1]))
