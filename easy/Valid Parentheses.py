"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 0.005914865857142857
        # table = {"(": 0, ")": 1, "[": 2, "]": 3, "{": 4, "}": 5}
        # stack = [s[0]]
        # idx = 1
        # N = len(s)
        # while idx < N:
        #     if stack and table[stack[-1]]+1 == table[s[idx]]:
        #         stack.pop()
        #     else:
        #         stack.append(s[idx])
        #     idx += 1
        # return False if stack else True

        # code refactoring - 0.004202033571428572
        table = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in table:
                stack.append(char)
            elif stack and table[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("(("))
print(s.isValid(")("))


import timeit
avg_time = 0.
tests = [["()"],
         ["()[]{}"],
         ["(]"],
         ["([)]"],
         ["{[]}"],
         ["(("],
         [")("]]
for t in tests:
    avg_time += timeit.timeit(lambda: s.isValid(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
