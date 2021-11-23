class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 2
        local_n = 1
        while local_n + row - 1 < n:
            local_n += row
            row += 1
        return row-1


s = Solution()
print(s.arrangeCoins(1))
print(s.arrangeCoins(3))
print(s.arrangeCoins(6))
print(s.arrangeCoins(10))
print(s.arrangeCoins(14))
print(s.arrangeCoins(15))        



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

