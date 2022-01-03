class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 0.15043390728533268
        #ans = list()
        #for i in range(0, len(s), 2*k):
        #    sub = s[i: i+k][::-1] + s[i+k: i+k*2]
        #    ans.append("".join(sub))
        #return "".join(ans) 

        # code refactoring (R) 01 - 0.13875450659543276
        #ans = list(s)
        #for i in range(0, len(s), 2*k):
        #    ans[i: i+k] = s[i: i+k][::-1]
        #return "".join(ans)

        # code refactoring (R) 02 - 0.08347832038998604
        i = 0
        ans = ""
        while i < len(s):
            ans += s[i:i+k][::-1]
            ans += s[i+k:i+k+k]
            i += 2*k
        return ans


s = Solution()
print(s.reverseStr("abcdefg", 2))       # bacdfeg
print(s.reverseStr("abcd", 2))          # bacd
print(s.reverseStr("abcdefghij", 2))    # bacdfeghji
print(s.reverseStr("abcdefghij", 3))    # cbadefihgj
print(s.reverseStr("abc", 3))           # cba
print(s.reverseStr("abcdefg", 3))       # cbadefg
print(s.reverseStr("abcdefg", 4))       # dcbaefg
print(s.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))


if __name__ == '__main__':
    from timeit import Timer
    query = [["abcdefg", 2], ["abcd", 2], ["abcdefghij", 2], ["abcdefghij", 3], ["abc", 3], ["abcdefg", 3], ["abcdefg", 4], ["hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39]]
    t = Timer(f"for t in {query}: Solution().reverseStr(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

