class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        # 0.5672869747504592
        ans = [0, 1]
        for i in range(n-1):
            ans.append(ans[-2] + ans[-1])
        return ans[-1]

        # version2 - 0.6425016699358821
        #for i in range(n-1):
        #    ans[i%2] += ans[i%2-1]
        #return ans[n%2]


s = Solution()
print(s.fib(2))
print(s.fib(1))
print(s.fib(0))
print(s.fib(7))


if __name__ == '__main__':
    from timeit import Timer
    query = [i for i in range(30)]
    t = Timer(f"for t in {query}: Solution().fib(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

