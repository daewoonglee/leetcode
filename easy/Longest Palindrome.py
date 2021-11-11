class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = dict()
        for ch in s:
            if ch not in data:
                data[ch]=0
            data[ch]+=1
        ans = 0
        is_one = False
        for v in data.values():
            if v%2==0: ans += v
            else: ans += v-1; is_one = True
        return ans+1 if is_one else ans


s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("abcde"))
print(s.longestPalindrome("aaabbbccccdd"))
print(s.longestPalindrome("aaabccccdd"))

