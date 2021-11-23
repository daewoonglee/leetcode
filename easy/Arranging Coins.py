class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2.2403946528211236
        #row = 2
        #local_n = 1
        #while local_n + row - 1 < n:
        #    local_n += row
        #    row += 1
        #return row-1

        # code refactoring 01 (R) - 0.17164469324052334
        #left, right = 0, n
        #while left <= right:
        #    row = (right + left) // 2
        #    calc_n = row * (row + 1) // 2
        #    if calc_n < n: left = row+1
        #    elif calc_n > n: right = row-1
        #    else: return row
        #return right

        # code refactoring 02 (R) - 0.0451074680313468
        return int((2*n+0.25)**0.5-0.5)


s = Solution()
print(s.arrangeCoins(1))
print(s.arrangeCoins(3))
print(s.arrangeCoins(6))
print(s.arrangeCoins(10))
print(s.arrangeCoins(14))
print(s.arrangeCoins(15))        


if __name__ == '__main__':
    from timeit import Timer
    query = [1, 3, 6, 10, 14, 15, 100, 1000, 10000, 100000, 1000000]
    t = Timer(f"for t in {query}: Solution().arrangeCoins(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))


"""
n   return  rule
1   1       
2   1       2
-----------------
3   2       
4   2       
5   2       3
-----------------
6   3       
7   3       
8   3       
9   3       4
-----------------
10  4       
11  4       
12  4       
13  4       
14  4       5
-----------------
15  5       
20  5       6
-----------------
21  6       7
"""

