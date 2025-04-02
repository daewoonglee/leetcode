class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        N = len(nums)
        total_sum = sum(nums)
        unique_sum = sum(set(nums))
        expected_sum = N * (N+1) // 2
        return [total_sum - unique_sum, expected_sum - unique_sum]


s = Solution()
# print(s.findErrorNums([1,2,2,4])) # [2,3]
# print(s.findErrorNums([1,1])) # [1,2]
# print(s.findErrorNums([2,2])) # [2,1]
# print(s.findErrorNums([1,2,2])) # [2,3]
# print(s.findErrorNums([1,3,3])) # [3,2]
# print(s.findErrorNums([2,2,1])) # [2,3]
# print(s.findErrorNums([4,2,2,1])) # [2,3]
# print(s.findErrorNums([2,3,2])) # [2,1], 방향성 없이 중복되어 없어진 값을 찾아야 하는듯
# print(s.findErrorNums([5,4,3,2,1,1])) # [1,6]
print(s.findErrorNums([2,3,3,4,6,5])) # [3,1]
