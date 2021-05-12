class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 0.053523326999999996
        # global_profit = 0
        # local_profit = 0
        # lowest = prices[0]
        # largest = -1
        # for p in prices[1:]:
        #     if local_profit < p - lowest:
        #         largest = p
        #         local_profit = p - lowest
        #     elif p < lowest or p < largest:
        #         lowest = p
        #         global_profit += local_profit
        #         local_profit = 0
        # return global_profit + local_profit

        # 0.085622725
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 7
print(s.maxProfit([1, 2, 3, 4, 5]))     # 4
print(s.maxProfit([1, 2, 3, 1, 5]))     # 6
print(s.maxProfit([7, 6, 4, 3, 1]))     # 0
print(s.maxProfit([1, 3, 2, 4, 3, 10])) # 11
print(s.maxProfit([2, 1, 2, 0, 1]))     # 2


if __name__ == '__main__':
    from timeit import Timer
    query = [[7, 1, 5, 3, 6, 4],
             [1, 2, 3, 4, 5],
             [1, 2, 3, 1, 5],
             [7, 6, 4, 3, 1],
             [1, 3, 2, 4, 3, 10],
             [2, 1, 2, 0, 1]]
    t = Timer(f"for t in {query}: Solution().maxProfit(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
