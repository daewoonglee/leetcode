class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()

        dup_n = nums[0]
        idx = 1
        N = len(nums)
        while idx < N and dup_n != nums[idx]:
            dup_n = nums[idx]
            idx += 1

        loss_n = N
        for i, n in enumerate(nums[:idx] + nums[idx+1:]):
            if i + 1 != n:
                loss_n = i+1
                break
        return [dup_n, loss_n]


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
