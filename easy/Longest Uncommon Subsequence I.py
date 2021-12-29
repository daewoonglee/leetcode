class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        #if a == b:
        #    return -1
        # 0.036305010318756104
        #return len(a) if len(a) > len(b) else len(b)
        #
        # 0.04171966575086117 - function callback
        #return max(len(a), len(b))

        # code refactoring - 0.8633379116654396 (위 a==b 구현)
        N = len(a) if len(a) > len(b) else len(b)
        if len(a) == len(b):
            for ch_a, ch_b in zip(a, b):
                if ch_a != ch_b:
                    return N
            return -1
        return N


s = Solution()
print(s.findLUSlength("aaa", "bbb"))
print(s.findLUSlength("aaa", "ababa"))
print(s.findLUSlength("aaab", "ababab"))
print(s.findLUSlength("aaac", "ababa"))
print(s.findLUSlength("aabbb", "ccc"))
print(s.findLUSlength("aabbb", "aa"))
print(s.findLUSlength("aabbb", "aab"))


if __name__ == '__main__':
    from timeit import Timer
    query = [["aaa", "bbb"], ["aaa", "ababa"], ["aaab", "ababab"], ["aaac", "ababa"], ["aabbb", "ccc"], ["aabbb", "aa"], ["aabbb", "aab"], ["a"*1000, "a"*1000], ["a"*1000, "a"*999 + "b"]]
    t = Timer(f"for t in {query}: Solution().findLUSlength(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

