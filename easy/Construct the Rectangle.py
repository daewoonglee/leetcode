class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        nums = [1] + [d for d in range(2, area // 2 + 1) if area % d == 0] + [area]
        p = len(nums) // 2
        return [nums[p], nums[p]] if len(nums) % 2 == 1 else [nums[p], nums[p-1]]


s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(37))
print(s.constructRectangle(122122))
print(s.constructRectangle(3))

