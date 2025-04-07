class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if not ops: return m*n
        min_x, min_y = 40000, 40000
        for x, y in ops:
            if x < min_x: min_x = x
            if y < min_y: min_y = y
        return min_x * min_y



s = Solution()
print(s.maxCount(3, 3, [[2,2],[3,3]])) # 4
print(s.maxCount(3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]])) # 4
print(s.maxCount(3, 3, [])) # 9
print(s.maxCount(3, 3, [[2,3], [3,2]])) # 4
print(s.maxCount(3, 3, [[2,3]])) # 6
print(s.maxCount(40000, 40000, [[2,3]])) # 6
