"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 0.013750259799999998
        # table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # N = len(s)
        # idx = 0
        # answer = 0
        # while N-1 > idx:
        #     if table[s[idx]] < table[s[idx+1]]:
        #         answer += table[s[idx+1]] - table[s[idx]]
        #         idx += 2
        #     else:
        #         answer += table[s[idx]]
        #         idx += 1
        # return answer + table[s[-1]] if N > idx else answer

        # code refactoring - 0.0168344708
        # 매번 비교해야해서 원래 풀이보다 더 느림
        # MCMXC가 있으면, CM비교하고 {MX를 또 비교해서 값을 더하는 불필요 단계 추가}
        # table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # answer = table[s[-1]]
        # for i in range(len(s)-1):
        #     if table[s[i]] < table[s[i+1]]:
        #         answer -= table[s[i]]
        #     else:
        #         answer += table[s[i]]
        # return answer

        # code refactoring 02 - 0.0111070206
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans, p = 0, 'I'
        for c in s[::-1]:
            print(f"c: {c}")
            ans, p = ans - table[c] if table[c] < table[p] else ans + table[c], c
        return ans


s = Solution()
# print(s.romanToInt("III"))
print(s.romanToInt("IV"))
# print(s.romanToInt("IX"))
# print(s.romanToInt("LVIII"))
# print(s.romanToInt("MCMXCIV"))


# import timeit
# avg_time = 0.
# tests = ["III",
#          "IV",
#          "IX",
#          "LVIII",
#          "MCMXCIV"]
# for t in tests:
#     avg_time += timeit.timeit(lambda: s.romanToInt(t), number=10000)
# print(f'avg_time: {avg_time / len(tests)}')
