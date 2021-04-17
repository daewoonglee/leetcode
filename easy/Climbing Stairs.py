"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


from math import factorial
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1.618947117
        # ans = 0
        # s1, s2 = n, 0
        # while s1 >= 0:
        #     N = (s1 + s2)
        #     m = 1
        #     for n in [N-i for i in range(s1)]:
        #         m *= n
        #     ans += (m / factorial(s1))
        #     s1 -= 2
        #     s2 += 1
        # return int(ans)

        # 0.022250198
        # if n <= 2:
        #     return n
        # f1, f2 = 1, 2
        # for i in range(2, n):
        #     f1, f2 = f2, f1 + f2
        # return f2

        # 0.07060477700000001
        f = [1] * (n+1)
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[-1]


s = Solution()
print(s.climbStairs(1)) # 1
print(s.climbStairs(2)) # 2
print(s.climbStairs(3)) # 3
print(s.climbStairs(4)) # 5
print(s.climbStairs(5)) # 8
print(s.climbStairs(6)) # 13
print(s.climbStairs(200)) # 453973694165307964765228010065414416498688


if __name__ == '__main__':
    from timeit import Timer
    query = [1, 2, 3, 4, 5, 6, 7, 120, 200]
    t = Timer(f"for t in {query}: Solution().climbStairs(t)", "from __main__ import Solution")
    print(t.timeit(number=1000))
