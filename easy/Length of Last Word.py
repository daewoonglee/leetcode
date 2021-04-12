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
        # 1.7106201140000001
        ss = s.split()
        return len(ss[-1]) if ss else 0


s = Solution()
# print(s.lengthOfLastWord("Hello World"))
# print(s.lengthOfLastWord(""))
print(s.lengthOfLastWord("a"))
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord("a aaa aa"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["Hello World", "", "a", "a ", "a aaa a"]
    t = Timer(f"for t in {query}: Solution().lengthOfLastWord(t)", "from __main__ import Solution")
    print(t.timeit())
