class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        #mat_h, mat_w = len(mat), len(mat[0])
        #if r*c != mat_h*mat_w: return mat

        # 0.20071707852184772
        #ans = [[0 for _ in range(c)] for _ in range(r)]
        # code refactoring (copies, not create) - 0.1561039499938488
        #ans = [[0]*c for _ in range(r)]
        #for i in range(r*c):
        #    ans[i//c][i%c] = mat[i//mat_w][i%mat_w]
        #return ans

        # code refactoring - 0.17701717466115952
        #return [[mat[(i*c+j)//mat_w][(i*c+j)%mat_w] for j in range(c)] for i in range(r)]

        # code refactoring (R) - 0.08788875676691532
        #flat = [n for r in mat for n in r]
        # code refactoring (R) (작은 리스트 한정) - 0.07605184428393841
        flat = sum(mat, [])
        if r*c != len(flat): return mat
        return [flat[i:i+c] for i in range(0, len(flat), c)]


s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))
print(s.matrixReshape([[1,2],[3,4]], 2, 4))
print(s.matrixReshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 8))
print(s.matrixReshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 8, 2))
print(s.matrixReshape([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]], 4, 4))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[[1,2],[3,4]], 1, 4], [[[1,2],[3,4]], 2, 4], [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 8], [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 8, 2], [[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]], 4, 4]]
    t = Timer(f"for t in {query}: Solution().matrixReshape(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

