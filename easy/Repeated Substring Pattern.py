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
        for i in range(1, len(s)//2+1):
            if len(s) % i == 0:
                split_s = [s[j: j+i] for j in range(0, len(s), i)]
                if len(set(split_s)) == 1: return True
        return False


s = Solution()
#print(s.repeatedSubstringPattern("a"))
#print(s.repeatedSubstringPattern("aa"))
#print(s.repeatedSubstringPattern("ab"))
#print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("abac"))
print(s.repeatedSubstringPattern("abababac"))
#print(s.repeatedSubstringPattern("abcab"))
#print(s.repeatedSubstringPattern("aabaaba"))
#print(s.repeatedSubstringPattern("aaaaa"))
#print(s.repeatedSubstringPattern("abcabcabc"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["a", "aa", "ab", "abab", "abac", "abababac", "abcab", "aabaaba", "aaaaa", "abcabcabc"]
    t = Timer(f"for t in {query}: Solution().repeatedSubstringPattern(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

