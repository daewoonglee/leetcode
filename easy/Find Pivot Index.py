class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            right_sum -= n
            if left_sum == right_sum:
                return i
            left_sum += n
        return -1


s = Solution()
print(s.pivotIndex([1,7,3,6,5,6])) # 3
print(s.pivotIndex([1,2,3])) # -1
print(s.pivotIndex([2,1,-1])) # 0
