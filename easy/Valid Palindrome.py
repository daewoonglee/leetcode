class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = [ch.lower() for ch in s if ch.isalpha() or ch.isnumeric()]
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[-i-1]:
                return False
        return True


s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
print(s.isPalindrome("0P"))
