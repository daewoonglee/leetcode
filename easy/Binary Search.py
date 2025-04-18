class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except ValueError:
        #     return -1

        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                return mid
        return -1


s = Solution()
print(s.search([-1,0,3,5,9,12], 9)) # 4
print(s.search([-1,0,3,5,9,12], 2)) # -1
print(s.search([1], 1))
print(s.search([1], 0))
