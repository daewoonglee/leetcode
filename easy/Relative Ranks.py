class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        medal = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        idx_dic = {s: i for i, s in enumerate(score)}
        ans = [_ for _ in range(len(score))]
        sort_score = sorted(score, reverse=True)
        for i, s in enumerate(sort_score[:3]):
            ans[idx_dic[s]] = medal[i]
        for i, s in enumerate(sort_score[3:]):
            ans[idx_dic[s]] = str(i+4)
        return ans

s = Solution()
print(s.findRelativeRanks([5,4,1,2,3]))
print(s.findRelativeRanks([5,4,3,2,1]))
print(s.findRelativeRanks([1]))
 
