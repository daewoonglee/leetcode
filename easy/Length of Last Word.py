"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 0.359111319 - 20ms on leetcode site
        # ss = s.split()
        # return len(ss[-1]) if ss else 0

        # no use split method - 0.9108843489999999
        # ss = [""]
        # for ch in s:
        #     if ch.isspace():
        #         ss.append("")
        #     else:
        #         ss[-1] += ch
        # ss = [ch for ch in ss if ch != '']
        # return len(ss[-1]) if ss else 0

        # 0.415782654 - 20ms on leetcode site
        # return len(s.strip().split(' ')[-1])

        # 0.5393116490000001 - 16ms on leetcode site
        idx = len(s)-1
        cnt = 0
        while idx >= 0:
            if not s[idx].isspace():
                cnt += 1
            elif cnt:
                return cnt
            idx -= 1
        return cnt


s = Solution()
# print(s.lengthOfLastWord("Hello World"))    # 5
print(s.lengthOfLastWord(""))               # 0
print(s.lengthOfLastWord(" "))              # 0
print(s.lengthOfLastWord('  '))             # 0
# print(s.lengthOfLastWord("b "))             # 1
# print(s.lengthOfLastWord("a"))              # 1
print(s.lengthOfLastWord("a "))             # 1
# print(s.lengthOfLastWord("a aaa aa"))       # 2
print(s.lengthOfLastWord("b  a  "))         # 1


if __name__ == '__main__':
    from timeit import Timer
    query = ["Hello World", "", " ", "  ", "b ", "a", "a ", "a aaa a", "b  a  "]
    t = Timer(f"for t in {query}: Solution().lengthOfLastWord(t)", "from __main__ import Solution")
    print(t.timeit(number=100000))
