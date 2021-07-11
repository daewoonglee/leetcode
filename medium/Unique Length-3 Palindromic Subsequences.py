class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ans = {k: set() for k in set(s)}
        # 0.282495168
        for k in ans:
            i = s.index(k)
            for j in range(N-1, i+1, -1):
                if k == s[j]:
                    for word in set(s[i+1:j]):
                        ans[k].add(word)
                    break
        return sum([len(v) for v in ans.values()])


s = Solution()
print(s.countPalindromicSubsequence("abca"))   # 2
# print(s.countPalindromicSubsequence("aabca"))   # 3
# print(s.countPalindromicSubsequence("adc"))   # 0
# print(s.countPalindromicSubsequence("bbcbaba"))   # 4
# print(s.countPalindromicSubsequence("ababab"))   # 4
# print(s.countPalindromicSubsequence("abcaaaaaaaaaaaaaaaaaaaaaaaaaabca"))
# print(s.countPalindromicSubsequence("abcdefghabcdefgh"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["abca",
             "aabca",
             "adc",
             "bbcbaba",
             "ababab",
             "abcaaaaaaaaaaaaaaaaaaaaaaaaaabca"]
    t = Timer(f"for t in {query}: Solution().countPalindromicSubsequence(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
