class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_cnt = 0
        n_list = list(range(n+1))
        for i in range(2, n):
            if n_list[i] == -1:
                continue
            cnt = 2
            while i*cnt <= n:
                n_list[i*cnt] = -1
                cnt += 1
            total_cnt += 1
        return total_cnt


s = Solution()
print(s.countPrimes(10))
print(s.countPrimes(0))
print(s.countPrimes(1))
print(s.countPrimes(2))
print(s.countPrimes(20))
