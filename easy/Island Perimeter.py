class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        # 0.26883668545633554
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
        """

        """ 
        # code refactoring - 0.175175154581666
        def get_land(nodes):
            for i, rows in enumerate(nodes):
                for j, n in enumerate(rows):
                    if n: return [[i, j]]
            return None

        rows, cols = len(grid), len(grid[0])
        maps = [g[:] for g in grid]
        dfs = get_land(grid)
        ans = 0
        while dfs:
            x, y = dfs.pop()
            if not maps[x][y]: continue
            maps[x][y] = 0
            ans += 4
            if y-1 >= 0 and grid[x][y-1]:
                ans -= 1
                if maps[x][y-1]: dfs.append([x, y-1])
            if y+1 < cols and grid[x][y+1]:
                ans -= 1
                if maps[x][y+1]: dfs.append([x, y+1])
            if x+1 < rows and grid[x+1][y]:
                ans -= 1
                if maps[x+1][y]: dfs.append([x+1, y])
            if x-1 >= 0 and grid[x-1][y]:
                ans -= 1
                if maps[x-1][y]: dfs.append([x-1, y])
        return ans
        """

        """
        # code refactoring (R) - 0.1334824739024043
        perimeter = 0
        m = len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i==0 or grid[i-1][j] == 0: perimeter += 1
                    if i==m-1 or grid[i+1][j] == 0: perimeter += 1
                    if j==0 or grid[i][j-1] == 0 : perimeter += 1
                    if j==n-1 or grid[i][j+1] == 0: perimeter += 1
        return perimeter
        """

        # code refactoring (R) 02 - 0.11234854348003864
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i>0 and grid[i-1][j] == 1: perimeter -= 2
                    if j>0 and grid[i][j-1] == 1: perimeter -= 2
        return perimeter


s = Solution()
# print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(s.islandPerimeter([[1,0,1],[1,1,1]]))
print(s.islandPerimeter([[1,1],[1,1]]))
print(s.islandPerimeter([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))

if __name__ == '__main__':
    from timeit import Timer
    query = [[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], [[1,0,1],[1,1,1]], [[1,1],[1,1]], [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,    0],[0,0,0,0,0]]]
    t = Timer(f"for t in {query}: Solution().islandPerimeter(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

