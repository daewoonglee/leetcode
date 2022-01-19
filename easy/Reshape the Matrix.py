class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ans = [[0 for _ in range(c)] for _ in range(r)]
        mat_h, mat_w = len(mat), len(mat[0])
        print(f"ans: {ans}")
        print(f"h: {mat_h}, w: {mat_w}")

        if r*c != mat_h*mat_w: return mat
        for i, mat_r in enumerate(mat):
            for j, mat_c in enumerate(mat_r):
                # ans[i][j] = mat_c
                # j = i*2+j
                pass
        return ans


s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))

