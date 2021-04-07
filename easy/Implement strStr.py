"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = 'hello', needle = 'll'
Output: 2

Example 2:
Input: haystack = 'aaaaa', needle = 'bba'
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 3.371248084
        # N = len(needle)
        # for i in range(len(haystack)-N+1):
        #     if haystack[i: i+N] == needle:
        #         return i
        # return -1

        # code refactoring
        # 1.711348691
        if not needle:
            return 0
        try:
            index = haystack.index(needle)
        except:
            index = -1
        return index


s = Solution()
print(s.strStr('hello', 'll'))
print(s.strStr('aaaaa', 'baa'))
print(s.strStr('', ''))
print(s.strStr('aabaa', 'aa'))


if __name__ == '__main__':
    from timeit import Timer
    t = Timer("for t in [['hello', 'll'], ['aaaaa', 'baa'], ['', ''], ['aabaa', 'aa']]: Solution().strStr(*t)",
              "from __main__ import Solution")
    print(t.timeit())