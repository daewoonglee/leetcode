class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s

s = Solution()
print(s.reverseString(["H", "e", "l", "l", "o"]))
print(s.reverseString(["t", "e", "s", "t"]))
 
