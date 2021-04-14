"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


from itertools import zip_longest
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a > len_b:
            b = b.zfill(len_a)
        else:
            a = a.zfill(len_b)
            len_a = len(a)
        ans = ""
        d = 0
        for i in range(len_a-1, -1, -1):
            na, nb = int(a[i]), int(b[i])
            s = na + nb + d
            if s == 0:
                ans = "0" + ans
                d = 0
            elif s == 1:
                ans = "1" + ans
                d = 0
            elif s == 2:
                ans = "0" + ans
                d = 1
            else:
                ans = "1" + ans
                d = 1
        return "1" + ans if d else ans


s = Solution()
print(s.addBinary("11", "1"))       # 100
print(s.addBinary("1010", "1011"))  # 10101
print(s.addBinary("1000", "1"))     # 1001
print(s.addBinary("111", "111"))    # 1110
print(s.addBinary("10000000000", "111"))  # 10000000111
print(s.addBinary("1", "111"))  # 1000
