class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i, n in enumerate(nums[:-1]):
            if n == nums[i+1]:
                return True
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
print(s.containsDuplicate([1, 2, 3, 4]))
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
