class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        li = [[1]]
        for i in range(1, rowIndex+1):
            li.append([1])
            for j in range(i-1):
                li[-1].append(li[i-1][j] + li[i-1][j+1])
            li[-1].append(1)
        return li[-1]


s = Solution()
print(s.getRow(3))  # 1 3 3 1
