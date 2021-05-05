class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        li = [[1] * i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(len(li[i])-2):
                li[i][j+1] = li[i-1][j] + li[i-1][j+1]
        return li


s = Solution()
# print(s.generate(5))
# print(s.generate(9))
print(s.generate(1))
print(s.generate(2))
print(s.generate(3))
