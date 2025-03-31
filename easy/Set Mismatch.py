class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        plus = 1 if nums[0] == 1 else -1
        reverse = 1 if nums[-1] == 1 else 0
        pre_n = nums[0]
        for i, n in enumerate(nums[1:]):
            if pre_n == n:
                return [n, n+1] if reverse else [n, n+plus]
            pre_n = n
        return [-1, -1]


s = Solution()
print(s.findErrorNums([1,2,2,4])) # [2,3]
print(s.findErrorNums([1,1])) # [1,2]
print(s.findErrorNums([2,2])) # [2,1]
print(s.findErrorNums([1,2,2])) # [2,3]
print(s.findErrorNums([2,2,1])) # [2,3]
print(s.findErrorNums([4,2,2,1])) # [2,3]
print(s.findErrorNums([2,3,2])) # [2,1], 방향성 없이 중복되어 없어진 값을 찾아야 하는듯
