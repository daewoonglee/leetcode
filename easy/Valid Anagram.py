class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 0.06722059999999999
        # return sorted(s) == sorted(t)

        # code refactoring - 0.128549661
        cnt = dict()
        for c in s:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
        for c in t:
            if c not in cnt:
                return False
            cnt[c] -= 1
        for v in cnt.values():
            if v:
                return False
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("stressed", "desserts"))
print(s.isAnagram("elvis", "lives"))
print(s.isAnagram("elvis", "livee"))
print(s.isAnagram("abcdefg", "abcdefgh"))


if __name__ == '__main__':
    from timeit import Timer
    query = [["anagram", "nagaram"],
             ["stressed", "desserts"],
             ["elvis", "lives"],
             ["elvis", "livee"],
             ["abcdefg", "abcdefgh"]]
    t = Timer(f"for t in {query}: Solution().isAnagram(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
