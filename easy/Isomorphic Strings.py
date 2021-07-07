class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        log_s, log_t = {}, {}
        for c1, c2 in zip(s, t):
            if c1 not in log_s:
                log_s[c1] = len(log_s)
            if c2 not in log_t:
                log_t[c2] = len(log_t)
            if log_s[c1] != log_t[c2]:
                return False
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("fow", "baa"))
print(s.isIsomorphic("paper", "title"))
