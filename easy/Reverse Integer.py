"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-231 <= x <= 231 - 1
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 0.008033036375
        # r_x = int(str(x)[::-1][:-1])*-1 if x < 0 else int(str(x)[::-1])
        # return r_x if -2**31 <= r_x <= 2**31-1 else 0

        # code refactoring -> 0.019830493749999994
        MAX = int((2**31-1)/10)
        MIN = int(-2**31/10)
        flag = 1 if x > 0 else -1
        x *= flag
        rev = 0
        while x != 0:
            x, r = divmod(x, 10)
            # print(f"x: {x}, r: {r}, rev: {rev}, MAX: {(2**31-1)/10}, MIN: {-2**31/10}")
            if rev > MAX or rev == MAX and r > 7:
                return 0
            elif rev < MIN or rev == MIN and r < -8:
                return 0
            rev = rev * 10 + r
        return rev * flag
    

s = Solution()
# print(s.reverse(123))
# print(s.reverse(-123))
# print(s.reverse(120))
# print(s.reverse(0))
# print(s.reverse(90000))
# print(s.reverse(1534236469))
print(s.reverse(7463847412))
print(s.reverse(8463847412))


import timeit
avg_time = 0.
tests = [123,
         -123,
         120,
         0,
         90000,
         1534236469,
         7463847412,
         8463847412]
for t in tests:
    avg_time += timeit.timeit(lambda: s.reverse(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
