class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        # 0.04151136800646782
        #r = "".join(sorted(ransomNote))
        #m = "".join(sorted(magazine))
        #i = j = 0
        #while i < len(r) and j < len(m):
        #    if r[i] == m[j]:
        #        i += 1
        #        j += 1
        #    else:
        #        j += 1
        #return i == len(r)

        # code refactoring - 0.03525837394408882 
        #log = dict()
        #for r in ransomNote:
        #    if r not in log:
        #        log[r] = 1
        #    else:
        #        log[r] += 1
        #for m in magazine:
        #    if m in log:
        #        log[m] -= 1
        #return False if len([v for v in log.values() if v > 0]) else True

        # code refactoring (R) - 0.024485436035320163
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True


s = Solution()
print(s.canConstruct("aa", "baa"))
print(s.canConstruct("a", "bbbbbbbbbbbbbbbbbbbbbbba"))
print(s.canConstruct("aa", "a"))


if __name__ == '__main__':
    from timeit import Timer
    query = [["aa", "baa"], ["a", "bbbbbbbbbbbbbbbbbbbbbbba"], ["aa", "a"], ["aaaaaaaaaaaaaaaaaaaaaab", "b"]]
    t = Timer(f"for t in {query}: Solution().canConstruct(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

