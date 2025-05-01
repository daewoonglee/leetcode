class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def dfs(x, y):
            image[x][y] = color
            for mx, my in move:
                nx, ny = x+mx, y+my
                if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and image[nx][ny] == target:
                    visited[nx][ny] = 1
                    dfs(nx, ny)

        target = image[sr][sc]
        if target == color:
            return image

        M, N = len(image), len(image[0])
        move = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[0] * N for _ in image]
        dfs(sr, sc)
        return image


s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)) # [[2,2,2],[2,2,0],[2,0,1]]
print(s.floodFill([[0,0,0],[0,0,0]], 0, 0, 0)) # [[0,0,0],[0,0,0]]
print(s.floodFill([[1]], 0, 0, 0)) # [[0]]
print(s.floodFill([[1,1,1],[0,0,0]], 0, 0, 1)) # [[0,0,0],[0,0,0]]
