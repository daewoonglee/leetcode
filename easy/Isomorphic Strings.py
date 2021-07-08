class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 0.09776170799999999
        log_s, log_t = {}, {}
        for c1, c2 in zip(s, t):
            if c1 not in log_s:
                log_s[c1] = len(log_s)
            if c2 not in log_t:
                log_t[c2] = len(log_t)
            if log_s[c1] != log_t[c2]:
                return False
        return True

        # 0.08765810399999999
        # order = {}
        # rev = {}
        # for i in range(len(s)):
        #     if s[i] in order and order[s[i]] != t[i]:
        #         return False
        #     else:
        #         if t[i] in rev:
        #             return False
        #         else:
        #             order[s[i]] = t[i]
        #             rev[t[i]] = s[i]
        # return True

        # 0.080993188
        # mapping = {}
        # values = []
        # for i, c in enumerate(s):
        #     value = t[i]
        #     if c in mapping and mapping[c] != value:
        #         return False
        #     else:
        #         mapping[c] = value
        #
        # for v in mapping.values():
        #     if v not in values:
        #         values.append(v)
        #     else:
        #         return False
        # return True

        # 0.093506493
        # mapping = {}
        # for i, c in enumerate(s):
        #     if c not in mapping:
        #         if t[i] in mapping.values():
        #             return False
        #         mapping[c] = t[i]
        #     elif mapping[c] != t[i]:
        #         return False
        # return True

        # 0.077584771
        hashmap = {}
        mapval = {}
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] != t[i]:
                return False
            elif t[i] in mapval:
                return False
            else:
                hashmap[s[i]] = t[i]
                mapval[t[i]] = True
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("fow", "baa"))
print(s.isIsomorphic("paper", "title"))


if __name__ == '__main__':
    from timeit import Timer
    query = [["egg", "add"],
             ["foo", "bar"],
             ["fow", "baa"],
             ["paper", "title"],
             ["bbbaaaba", "aaabbbba"]]
    t = Timer(f"for t in {query}: Solution().isIsomorphic(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
