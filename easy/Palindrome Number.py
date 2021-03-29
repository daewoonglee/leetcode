"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.


Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Constraints:
-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # using str version
        # x = str(x)
        # N = len(x)
        # if N % 2 == 0:
        #     return True if x[:N//2] == x[N//2:][::-1] else False
        # else:
        #     return True if x[:N//2] == x[N//2+1:][::-1] else False

        # without converting int to str
        if x < 0:
            return False
        li = []
        while x != 0:
            x, r = divmod(x, 10)
            li.append(r)
        N = len(li)
        if N % 2 == 0:
            return True if li[:N//2] == li[N//2:][::-1] else False
        else:
            return True if li[:N//2] == li[N//2+1:][::-1] else False

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(-101))
print(s.isPalindrome(1001))
print(s.isPalindrome(10001))
print(s.isPalindrome(1000021))
