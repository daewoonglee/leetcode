class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        mat_h, mat_w = len(mat), len(mat[0])
        if r*c != mat_h*mat_w: return mat

        ans = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r*c):
            ans[i//c][i%c] = mat[i//mat_w][i%mat_w]
        return ans


s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))
print(s.matrixReshape([[1,2],[3,4]], 2, 4))
print(s.matrixReshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 8))
print(s.matrixReshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 8, 2))
print(s.matrixReshape([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]], 4, 4))
