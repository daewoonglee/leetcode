class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        L, R = 0, len(height)-1
        while L < R:
            if height[L] < height[R]:
                value = height[L] * (R-L)
                L += 1
            else:
                value = height[R] * (R-L)
                R -= 1

            if ans < value:
                ans = value
        return ans


s = Solution()
# print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
# print(s.maxArea([1,1])) # 1
print(s.maxArea([1,2,3,4,5,6,5,4,3])) # 18
