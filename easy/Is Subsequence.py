class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 0.06754814414307475
        #i = 0
        #N = len(s)
        #for ch in t:
        #    if i == N:
        #        break
        #    if s[i] == ch:
        #        i += 1
        #return i == len(s)

        # code refactoring (R) - 0.09510712698101997
        for i in s:
            j = t.find(i)
            if j == -1:
                return False
            else:
                # 메모리할당이 다시 일어나서 느림 
                # 접근방법 참고 겸 기재 
                t = t[j+1:]
        return True


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("abc", "ahchb"))
print(s.isSubsequence("aa", "a"))
print(s.isSubsequence("aa", "aaa"))
print(s.isSubsequence("", "a"))


if __name__ == '__main__':
    from timeit import Timer
    query = [["abc", "ahbgdc"], ["abc", "ahchb"], ["aa", "a"], ["aa", "aaa"], ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "abbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]]
    t = Timer(f"for t in {query}: Solution().isSubsequence(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

