class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return len(a) if len(a) > len(b) else len(b)


s = Solution()
print(s.findLUSlength("aaa", "bbb"))
print(s.findLUSlength("aaa", "ababa"))
print(s.findLUSlength("aaab", "ababab"))
print(s.findLUSlength("aaac", "ababa"))
print(s.findLUSlength("aabbb", "ccc"))
print(s.findLUSlength("aabbb", "aa"))
print(s.findLUSlength("aabbb", "aab"))


