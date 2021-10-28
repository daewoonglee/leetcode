class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = "".join(sorted(list(s)))
        t = "".join(sorted(list(t)))
        for w1, w2 in zip(s, t):
            if w1 != w2:
                return w2
        return t[-1]
            
        
s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("", "y"))
print(s.findTheDifference("a", "aa"))
print(s.findTheDifference("ae", "aea"))

