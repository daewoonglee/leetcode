class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #version1 - 0.14672745391726494
        #return " ".join([line[::-1] for line in s.split()])

        #version2 - 직접구현 0.7739312127232552
        space_idx = [i for i, ch in enumerate(s) if ch==" "] + [len(s)]

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


if __name__ == '__main__':
    from timeit import Timer
    query = ["Let's take LeetCode contest", "God Ding", "g", "a"*100, "a " * 100]
    t = Timer(f"for t in {query}: Solution().reverseWords(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

