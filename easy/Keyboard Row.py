class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 0.19772800616919994
        #k_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        #ans = []
        #dic = {i: [] for i in range(len(k_rows))}
        #for word in words:
        #    w = word[0].lower()
        #    if w in k_rows[0]:
        #        idx = 0
        #    elif w in k_rows[1]:
        #        idx = 1
        #    else:
        #        idx = 2
        #    dic[idx].append(word)

        #for k, v_li in dic.items():
        #    k_row = k_rows[k]
        #    for values in v_li:
        #        N = len(values)-1
        #        cnt = 0
        #        for v in values[1:].lower():
        #            if v in k_row:
        #                cnt += 1
        #        if cnt == N:
        #            ans.append(values)
        #return ans

        # 0.07887180242687464
        k_rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        ans = []
        for word in words:
            s_word = set(word.lower())
            if s_word <= k_rows[0] or s_word <= k_rows[1] or s_word <= k_rows[2]:
                ans.append(word)
        return ans


s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))


if __name__ == '__main__':
    from timeit import Timer
    query = [["Hello", "Alaska", "Dad", "Peace"], ["a"*100, "b"*100, "c"*100]]
    t = Timer(f"for t in {query}: Solution().findWords(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

