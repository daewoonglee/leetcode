class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get_land(nodes):
            for node in nodes:
                for n in node:
                    if n[2]:
                        return [n]
            return None
            
        rows, cols = len(grid), len(grid[0])
        searched = [[[i, j, 1, 0] if r else [i, j, 0, 0] for j, r in enumerate(row)] for i, row in enumerate(grid)]
        dfs = get_land(searched)
        ans = 0
        while dfs:
            x, y, g, f = dfs.pop()
            searched[x][y][-1] = 1
            cnt = 0
            if g and not f:
                if y-1 >= 0 and searched[x][y-1][2]:
                    cnt += 1
                    if not searched[x][y-1][-1]: dfs.append(searched[x][y-1])
                if y+1 < cols and searched[x][y+1][2]:
                    cnt += 1
                    if not searched[x][y+1][-1]: dfs.append(searched[x][y+1])
                if x+1 < rows and searched[x+1][y][2]:
                    cnt += 1
                    if not searched[x+1][y][-1]: dfs.append(searched[x+1][y])
                if x-1 >= 0 and searched[x-1][y][2]:
                    cnt += 1
                    if not searched[x-1][y][-1]: dfs.append(searched[x-1][y])
                ans += 4 - cnt
        return ans


s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

