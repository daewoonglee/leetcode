class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = dict()
        for i, ch in enumerate(s):
            if ch not in data:
                data[ch] = list()
            data[ch].append(i)
        
        li = [v[0] for v in data.values() if len(v) == 1]
        return min(li) if li else -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))

