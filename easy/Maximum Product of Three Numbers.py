class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2]*nums[-3] if nums[-1]*nums[-2]*nums[-3] > nums[0]*nums[1]*nums[-1] else nums[0]*nums[1]*nums[-1]


s = Solution()
# print(s.maximumProduct([1,2,3])) # 6
# print(s.maximumProduct([1,2,3,4])) # 24
# print(s.maximumProduct([-1,-2,-3])) # -6
# print(s.maximumProduct([-100,-98,-1,2,3,4])) # 39200
# print(s.maximumProduct([-100,-1,10,10,10])) # 1000
# print(s.maximumProduct([-5,-4,-3,-2,-1])) # -6
# print(s.maximumProduct([-8,-7,-2,10,20])) # 1120
# print(s.maximumProduct([-5,-1,0,0,3,4])) # 20
print(s.maximumProduct([-984,-960,-959,951,969,999]))
