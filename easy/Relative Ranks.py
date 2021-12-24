class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # 0.33279251493513584
        #medal = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        #idx_dic = {s: i for i, s in enumerate(score)}
        #ans = [_ for _ in range(len(score))]
        #sort_score = sorted(score, reverse=True)
        #for i, s in enumerate(sort_score[:3]):
        #    ans[idx_dic[s]] = medal[i]
        #for i, s in enumerate(sort_score[3:]):
        #    ans[idx_dic[s]] = str(i+4)
        #return ans

        # code refactoring (R) - 0.28162588458508253
        medal = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        sort_score = sorted(score, reverse=True)
        idx_dic = {s: str(i+4) for i, s in enumerate(sort_score[3:])}
        for i, s in enumerate(sort_score[:3]):
            idx_dic[s] = medal[i]
        return [idx_dic[s] for s in score] # list(map(idx_dic.get, score))


s = Solution()
print(s.findRelativeRanks([5,4,1,2,3]))
print(s.findRelativeRanks([5,4,3,2,1]))
print(s.findRelativeRanks([1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[5,4,1,2,3], [5,4,3,2,1], [1], [i+1 for i in range(40)], [i for i in range(40, 1, -1)]]
    t = Timer(f"for t in {query}: Solution().findRelativeRanks(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
 
