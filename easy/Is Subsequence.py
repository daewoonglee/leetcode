class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        for ch in t:
            if i == len(s):
                break
            if s[i] == ch:
                i += 1
        return i == len(s)
        

s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("abc", "ahchb"))

