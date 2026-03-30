class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = [0] * len(height)
        for i, h in enumerate(height):
            for j in range(i):
                area[j] = max(area[j], min(h, height[j])*(i-j))
        print(area)
        return max(area)


s = Solution()
# print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
# print(s.maxArea([1,1])) # 1
print(s.maxArea([5, 8, 9, 10, 11, 12, 10, 9, 8, 8, 8, 8, 8, 8, 8, 13])) # 144
