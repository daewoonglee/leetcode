class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("stressed", "desserts"))
print(s.isAnagram("elvis", "lives"))
print(s.isAnagram("elvis", "livee"))
print(s.isAnagram("abcdefg", "abcdefgh"))
