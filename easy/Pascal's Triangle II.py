class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 0.271169977
        # li = [[1]]
        # for i in range(1, rowIndex+1):
        #     li.append([1])
        #     for j in range(i-1):
        #         li[-1].append(li[i-1][j] + li[i-1][j+1])
        #     li[-1].append(1)
        # return li[-1]

        # code refactoring 01 - 0.172647976
        # li = [1]
        # for i in range(1, rowIndex+1):
        #     row = li[:]
        #     for j in range(i-1):
        #         row[j+1] = li[j] + li[j+1]
        #     row.append(1)
        #     li = row[:]
        # return li

        # code refactoring 02 (R) - 0.136601149
        li = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                li[j] += li[j-1]
        return li


s = Solution()
print(s.getRow(3))  # 1 3 3 1
print(s.getRow(4))  # 1 4 6 4 1
print(s.getRow(0))
print(s.getRow(1))


if __name__ == '__main__':
    from timeit import Timer
    query = [5, 9, 1, 2, 3, 30, 33]
    t = Timer(f"for t in {query}: Solution().getRow(t)", "from __main__ import Solution")
    print(t.timeit(number=1000))
