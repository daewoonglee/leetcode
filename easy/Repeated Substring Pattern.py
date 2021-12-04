class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 0.2537928009405732
        #for i in range(1, len(s)//2+1):
        #    split_s = [s[j: j+i] for j in range(0, len(s), i)]
        #    if len(set(split_s)) == 1: return True
        #return False
        
        # code refactoring - 0.21546904556453228 
        #for i in range(1, len(s)//2+1):
        #    if len(s) % i == 0:
        #        split_s = [s[j: j+i] for j in range(0, len(s), i)]
        #        if len(set(split_s)) == 1: return True
        #return False

        # code refactoring 02 - 0.154229449108243
        #N = len(s)
        #li = []
        #for i in range(1, N//2+1):
        #    if N % i == 0:
        #        li.append(s[:i])
        #        for j in range(i, N, i):
        #            li.append(s[j:j+i])
        #            if li[-1] != li[-2]: break
        #        if li[-1] == li[-2]: return True
        #        # clear time complexity = O(N)
        #        li.clear()
        #return False

        # code refactoring 02-1 - 0.14705622009932995
        #N = len(s)
        #for i in range(1, N//2+1):
        #    if N % i == 0:
        #        li = [s[:i]]
        #        for j in range(i, N, i):
        #            li.append(s[j:j+i])
        #            if li[-1] != li[-2]: break
        #        if li[-1] == li[-2]: return True
        #return False

        # code refactoring (R) - 0.030461512506008148        
        return s in (s+s)[1:-1]


s = Solution()
#print(s.repeatedSubstringPattern("a"))
#print(s.repeatedSubstringPattern("aa"))
#print(s.repeatedSubstringPattern("ab"))
#print(s.repeatedSubstringPattern("abab"))
#print(s.repeatedSubstringPattern("abac"))
#print(s.repeatedSubstringPattern("abababac"))
#print(s.repeatedSubstringPattern("ababab"))
#print(s.repeatedSubstringPattern("abcab"))
#print(s.repeatedSubstringPattern("aabaaba"))
print(s.repeatedSubstringPattern("aaaaa"))
print(s.repeatedSubstringPattern("abcabcabc"))
print(s.repeatedSubstringPattern("abacabac"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["a", "aa", "ab", "abab", "abac", "abababac", "abcab", "aabaaba", "aaaaa", "abcabcabc"]
    t = Timer(f"for t in {query}: Solution().repeatedSubstringPattern(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

