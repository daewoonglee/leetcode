"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 0.01481821371428571
        # strs_t = [s for s in zip(*strs)]
        # if not strs_t:
        #     return ""
        # ans = []
        # for s in strs_t:
        #     if len(set(s)) == 1:
        #         ans += s[0]
        #     else:
        #         break
        # return ''.join(ans)

        # code refactoring - 0.011319861714285716
        ans = []
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            ans += s[0]
        return "".join(ans) if ans else ""


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix(["aaabbbb", "aacbbbb", "aadbbbb"]))
print(s.longestCommonPrefix(["a", ""]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["dog", "dag"]))
print(s.longestCommonPrefix(["flower", "fkow"]))
print(s.longestCommonPrefix(["a"]))


import timeit
avg_time = 0.
tests = [["flower", "flow", "flight"],
         ["dog", "racecar", "car"],
         ["aaabbbb", "aacbbbb", "aadbbbb"],
         ["a", ""],
         [],
         ["dog", "dag"],
         ["flower", "fkow"]]
for t in tests:
    avg_time += timeit.timeit(lambda: s.longestCommonPrefix(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
