class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        r = "".join(sorted(ransomNote))
        m = "".join(sorted(magazine))
        i = j = 0
        while i < len(r) and j < len(m):
            if r[i] == m[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(r)


s = Solution()
print(s.canConstruct("aa", "baa"))
print(s.canConstruct("a", "bbbbbbbbbbbbbbbbbbbbbbba"))

