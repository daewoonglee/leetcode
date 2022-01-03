class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = list()
        for i in range(0, len(s), 2*k):
            sub = s[i: i+k][::-1] + s[i+k: i+k*2]
            ans.append("".join(sub))
        return "".join(ans) 


s = Solution()
print(s.reverseStr("abcdefg", 2))       # bacdfeg
print(s.reverseStr("abcd", 2))          # bacd
print(s.reverseStr("abcdefghij", 2))    # bacdfeghji
print(s.reverseStr("abcdefghij", 3))    # cbadefihgj
print(s.reverseStr("abc", 3))           # cba
print(s.reverseStr("abcdefg", 3))       # cbadefg
print(s.reverseStr("abcdefg", 4))       # dcbaefg
print(s.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))

