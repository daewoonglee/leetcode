class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2.952757444
        # total_cnt = 0
        # n_list = list(range(n+1))
        # for i in range(2, n):
        #     if n_list[i] == -1:
        #         continue
        #     idx = i * 2
        #     while idx <= n:
        #         if n_list[idx] != -1:
        #             n_list[idx] = -1
        #         idx += i
        #     total_cnt += 1
        # return total_cnt

        # code refactoring 01 - 1.866156606
        # if n <= 1:
        #     return 0
        # N = int(n ** 0.5)
        # n_list = [1] * n
        # # print(f"n: {n}, N: {N}, n_list: {n_list}")
        # for i in range(2, N+1):
        #     # print(f"i: {i}, n_list: {n_list}")
        #     if not n_list[i]:
        #         continue
        #     idx = i * 2
        #     while idx < n:
        #         if n_list[idx]:
        #             n_list[idx] = 0
        #         idx += i
        # return sum(n_list) - 2

        # code refactoring 02 - 0.848626818
        # if n <= 2:
        #     return 0
        # is_prime = [1] * n
        # for i in range(2, int(n ** 0.5) + 1):
        #     if is_prime[i]:
        #         for j in range(i+i, n, i):
        #             is_prime[j] = 0
        # return sum(is_prime) - 2

        # code refactoring (R) - 0.388370085
        if n <= 2:
            return 0
        is_prime = [1] * n
        is_prime[:2] = [0, 0]
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # is_prime[i+i:n:i] = [0] * len(is_prime[i+i:n:i])
                is_prime[i+i:n:i] = [0] * ((n-2*i-1) // i+1)
        return sum(is_prime)


s = Solution()
# print(s.countPrimes(10))    # 4
# print(s.countPrimes(0))     # 0
# print(s.countPrimes(1))     # 0
# print(s.countPrimes(2))     # 0
print(s.countPrimes(20))    # 8
# print(s.countPrimes(100))   # 25
# print(s.countPrimes(1000))  # 168
#
#
# if __name__ == '__main__':
#     from timeit import Timer
#     query = [10, 0, 1, 2, 20, 100, 1000]
#     t = Timer(f"for t in {query}: Solution().countPrimes(t)", "from __main__ import Solution")
#     print(t.timeit(number=10000))
