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
        l = 1
        while l <= n:
            g = (l+n) // 2
            res = guess(ans, g)
            if res == -1:
                n = g-1
            elif res == 1:
                l = g+1
            else:
                break
        return g


s = Solution()
print(s.guessNumber(10, 6))
#print(s.guessNumber(11, 5))

