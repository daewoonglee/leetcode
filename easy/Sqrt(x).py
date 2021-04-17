"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:
0 <= x <= 231 - 1
"""


import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 0.03201561
        # return int(math.sqrt(x))

        # Implement integer sqrt method 01 - 0.103219589
        # p = 1
        # while p**2 <= x:
        #     p += 1
        # return p-1

        # Newton–Raphson method - 0.11574681299999999
        # pre_x, cur_x = 0, 5
        # while 1:
        #     cur_x = cur_x - ((cur_x**2)-x) / (2*cur_x)
        #     if int(cur_x) != pre_x:
        #         pre_x = int(cur_x)
        #     else:
        #         break
        # return pre_x

        # code refactoring 01 - 0.029433162000000002
        return int(x**0.5)


s = Solution()
# print(s.mySqrt(0))
# print(s.mySqrt(1))
# print(s.mySqrt(2))
# print(s.mySqrt(3))
# print(s.mySqrt(4))
# print(s.mySqrt(8))
print(s.mySqrt(147))
# print(s.mySqrt(1470))


# if __name__ == '__main__':
#     from timeit import Timer
#     query = [0, 1, 2, 3, 4, 8, 147]
#     t = Timer(f"for t in {query}: Solution().mySqrt(t)", "from __main__ import Solution")
#     print(t.timeit(number=10000))
