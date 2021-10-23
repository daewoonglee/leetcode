# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(p, n):
    if p < n:
        return -1
    elif p > n:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n, ans):
        """
        :type n: int
        :rtype: int
        """
        # 0.21728841704316437
        # l = 1
        # while l <= n:
        #     g = (l+n) // 2
        #     res = guess(ans, g)
        #     if res == -1:
        #         n = g-1
        #     elif res == 1:
        #         l = g+1
        #     else:
        #         break
        # return g

        # code refactoring (R) - 0.2951773030217737
        l = 1
        while l <= n:
            p1 = l + (n-l) // 3
            p2 = n - (n-l) // 3

            g1 = guess(ans, p1)
            g2 = guess(ans, p2)

            if g1 == 0:
                return p1
            elif g2 == 0:
                return p2

            if g1 == -1:
                n = p1 - 1
            elif g2 == 1:
                l = p2 + 1
            else:
                l = p1 + 1
                n = p2 - 1


s = Solution()
print(s.guessNumber(10, 6))
print(s.guessNumber(11, 5))
print(s.guessNumber(2, 1))
print(s.guessNumber(1, 1))
print(s.guessNumber(10000000, 2))


if __name__ == '__main__':
    from timeit import Timer
    query = [[10, 6], [11, 5], [2, 1], [1, 1], [10000000, 2], [1000000000, 10000000], [100000000000000, 1]]
    t = Timer(f"for t in {query}: Solution().guessNumber(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

