class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 5.229325383901596
        # return [bin(i)[2:].count("1") for i in range(n+1)]

        # code refactoring - 1.5244826506823301        
        # N = 0
        # while 2**N < n:
        #     N += 1
        # li = [0, 1]
        # for _ in range(N):
        #     li += [i+1 for i in li]
        # return li[:n+1]

        # code refactoring (R) - 0.8218544516712427
        # li = [0]
        # while len(li) < n+1:
        #     li += [i+1 for i in li]
        # return li[:n+1]

        # code refactoring (R) - 2.0805573109537363
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = (i & 1) + dp[i >> 1]
        return dp


s = Solution()
#print(s.countBits(0))
#print(s.countBits(1))
#print(s.countBits(2))
#print(s.countBits(3))
#print(s.countBits(4))
#print(s.countBits(5))
#print(s.countBits(6))
print(s.countBits(9))
print(s.countBits(16))


if __name__ == '__main__':
    from timeit import Timer
    query = [0, 1, 2, 3, 4, 5, 6, 8, 16, 1666]
    t = Timer(f"for t in {query}: Solution().countBits(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

