class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        non_zero = zero = 0
        while N > non_zero:
            temp = nums[non_zero]
            nums[non_zero] = nums[zero]
            nums[zero] = temp
            while zero < N and nums[zero]:
                zero += 1
            non_zero = zero + 1
            while non_zero < N and not nums[non_zero]:
                non_zero += 1
        return nums


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
print(s.moveZeroes([0, 0, 1, 3, 12]))
print(s.moveZeroes([1, 3, 12, 0, 0]))
print(s.moveZeroes([1, 0, 0, 2, 0]))
print(s.moveZeroes([1, 2, 0, 3, 0]))
print(s.moveZeroes([1]))
