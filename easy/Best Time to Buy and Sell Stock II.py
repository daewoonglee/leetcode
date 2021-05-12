class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        global_profit = 0
        local_profit = 0
        lowest = prices[0]
        largest = -1
        for p in prices[1:]:
            if local_profit < p - lowest:
                local_profit = p - lowest
                largest = p
            elif p < lowest or p < largest:
                lowest = p
                global_profit += local_profit
                local_profit = 0
        return global_profit + local_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 7
print(s.maxProfit([1, 2, 3, 4, 5]))     # 4
print(s.maxProfit([7, 6, 4, 3, 1]))     # 0
print(s.maxProfit([1, 3, 2, 4, 3, 10])) # 11
print(s.maxProfit([2, 1, 2, 0, 1]))     # 2
