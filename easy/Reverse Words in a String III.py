class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #version1
        #return " ".join([line[::-1] for line in s.split()])

        #version2 - 직접구현
        white_space = ord(" ")
        space_idx = [i for i, ch in enumerate(s) if ord(ch)==white_space] + [len(s)]

        ans = ""
        pre_idx = -1
        for si in space_idx:
            sub_arr = s[pre_idx+1: si]
            for i in range(len(sub_arr)-1, -1, -1):
                ans += sub_arr[i]
            ans += " "
            pre_idx = si
        return ans[:-1]


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords("God Ding"))       
print(s.reverseWords("g"))
 
