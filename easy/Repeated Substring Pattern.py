class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 4: return len(set(s)) == 1
        for i in range(1, len(s)//2+1):
            split_s = [s[j: j+i] for j in range(0, len(s), i)]
            if len(set(split_s)) == 1: return True
        return False


s = Solution()
#print(s.repeatedSubstringPattern("a"))
#print(s.repeatedSubstringPattern("aa"))
#print(s.repeatedSubstringPattern("ab"))
#print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("abac"))
print(s.repeatedSubstringPattern("abababac"))
#print(s.repeatedSubstringPattern("abcab"))
#print(s.repeatedSubstringPattern("aabaaba"))
#print(s.repeatedSubstringPattern("aaaaa"))
#print(s.repeatedSubstringPattern("abcabcabc"))

