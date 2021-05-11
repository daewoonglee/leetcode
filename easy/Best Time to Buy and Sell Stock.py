class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # brute force
        # max_price = 0
        # N = len(prices)
        # for i in range(N-1):
        #     for j in range(i+1, N):
        #         if max_price < prices[j] - prices[i]:
        #             max_price = prices[j] - prices[i]
        # return max_price

        # 0.22602059400000002
        # min_n, max_n = [], []
        # idx = 0
        # N = len(prices)-1
        # while idx < N:
        #     if prices[idx] < prices[idx+1]:
        #         min_n.append(prices[idx])
        #         max_n.append(prices[idx+1])
        #         idx += 2
        #         break
        #     idx += 1
        # if not max_n:
        #     return 0
        #
        # while idx < N:
        #     if prices[idx] < min_n[-1] and prices[idx] < prices[idx+1]:
        #         min_n.append(prices[idx])
        #         max_n.append(prices[idx+1])
        #         idx += 1
        #     elif max_n[-1] < prices[idx]:
        #         max_n[-1] = prices[idx]
        #     idx += 1
        # if idx <= N and max_n[-1] < prices[idx]:
        #     max_n[-1] = prices[idx]
        # return max([n2-n1 for n1, n2 in zip(min_n, max_n)])

        # code refactoring 01 - 0.14248462399999998
        # profit = 0
        # lowest = prices[0]
        # for p in prices[1:]:
        #     if p < lowest:
        #         lowest = p
        #     else:
        #         profit = max(p-lowest, profit)
        # return profit

        # code refactoring 02 - 0.09024157799999999
        profit = 0
        lowest = prices[0]
        for p in prices[1:]:
            if p < lowest:
                lowest = p
            elif profit < p-lowest:
                profit = p-lowest
        return profit


s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
# print(s.maxProfit([7, 6, 4, 3, 1]))     # 0
# print(s.maxProfit([2, 4, 3, 2, 1, 7]))  # 6
# print(s.maxProfit([4, 2, 1, 5, 1, 7]))  # 6
# print(s.maxProfit([1, 2, 3, 4, 5, 7]))  # 6
# print(s.maxProfit([1, 1, 1, 1, 7, 0]))  # 6
# print(s.maxProfit([3, 2, 6, 5, 0, 3]))  # 4
# print(s.maxProfit([2, 1, 2, 1, 0, 1, 2])) # 2
print(s.maxProfit([9, 8, 9, 8, 7, 8, 9, 0, 5])) # 5
print(s.maxProfit([2, 1, 2, 1, 0, 1, 2, 1, 3])) # 3
print(s.maxProfit([2, 7, 1, 4, 11]))    # 10


if __name__ == '__main__':
    from timeit import Timer
    query = [[7, 1, 5, 3, 6, 4],
             [7, 6, 4, 3, 1],
             [2, 4, 3, 2, 1, 7],
             [4, 2, 1, 5, 1, 7],
             [1, 2, 3, 4, 5, 7],
             [1, 1, 1, 1, 7, 0],
             [3, 2, 6, 5, 0, 3],
             [2, 1, 2, 1, 0, 1, 2],
             [9, 8, 9, 8, 7, 8, 9, 0, 5],
             [2, 1, 2, 1, 0, 1, 2, 1, 3],
             [2, 7, 1, 4, 11]]
    t = Timer(f"for t in {query}: Solution().maxProfit(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
