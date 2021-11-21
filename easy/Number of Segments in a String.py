class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())


s = Solution()
print(s.countSegments("Hello, my name is John"))
print(s.countSegments("Hello"))
print(s.countSegments("love live! mu'sic forever"))
print(s.countSegments(""))
        
