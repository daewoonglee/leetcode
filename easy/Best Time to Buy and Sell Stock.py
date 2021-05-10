class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_price = 0
        # N = len(prices)
        # for i in range(N-1):
        #     for j in range(i+1, N):
        #         if max_price < prices[j] - prices[i]:
        #             max_price = prices[j] - prices[i]
        # return max_price

        min_n, max_n = 0, 0
        idx = 0
        N = len(prices)-1
        while idx < N:
            if prices[idx] < prices[idx+1]:
                min_n = prices[idx]
                max_n = prices[idx+1]
                idx += 2
                break
            idx += 1
        if max_n == 0:
            return 0

        while idx <= N:
            if prices[idx] > max_n:
                max_n = prices[idx]
            elif prices[idx] < min_n and idx < N and prices[idx] < prices[idx+1] and max_n - min_n <= prices[idx+1] - prices[idx]:
                min_n = prices[idx]
                max_n = prices[idx+1]
                idx += 1
            idx += 1
        return max_n - min_n


s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
# print(s.maxProfit([7, 6, 4, 3, 1]))
# print(s.maxProfit([2, 4, 3, 2, 1, 7]))
# print(s.maxProfit([4, 2, 1, 5, 1, 7]))
# print(s.maxProfit([1, 2, 3, 4, 5, 7]))
# print(s.maxProfit([1, 1, 1, 1, 7, 0]))
# print(s.maxProfit([3, 2, 6, 5, 0, 3]))
# print(s.maxProfit([2, 1, 2, 1, 0, 1, 2]))
# print(s.maxProfit([2, 1, 2, 1, 0, 1, 2, 1, 3]))
print(s.maxProfit([2, 7, 1, 4, 11]))
