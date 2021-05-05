class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 1.185275066
        # li = [[1] * i for i in range(1, numRows+1)]
        # for i in range(2, numRows):
        #     for j in range(len(li[i])-2):
        #         li[i][j+1] = li[i-1][j] + li[i-1][j+1]
        # return li

        # code refactoring - 1.0492544510000001
        res = [[1]]
        for i in range(1, numRows):
            res.append([1])
            for j in range(len(res[-2]) - 1):
                res[-1].append(res[-2][j] + res[-2][j + 1])
            res[-1].append(1)
        return res


s = Solution()
# print(s.generate(5))
# print(s.generate(9))
# print(s.generate(30))
print(s.generate(1))
print(s.generate(2))
print(s.generate(3))


if __name__ == '__main__':
    from timeit import Timer
    query = [5, 9, 1, 2, 3, 30]
    t = Timer(f"for t in {query}: Solution().generate(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
