class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 0.1739299362525344
        #data = dict()
        #for i, ch in enumerate(s):
        #    if ch not in data:
        #        data[ch] = list()
        #    data[ch].append(i)
        #
        #li = [v[0] for v in data.values() if len(v) == 1]
        #return min(li) if li else -1

        # code refactoring - 0.17127462290227413
        #data = dict()
        #for i, ch in enumerate(s):
        #    if ch not in data:
        #        data[ch] = [i, 0]
        #    data[ch][-1] += 1

        #li = [v[0] for v in data.values() if v[-1] == 1]
        #return min(li) if li else -1        

        # code refactoring (R) - 0.10413515707477927
        #data = dict()
        #presented = set()
        #for i, ch in enumerate(s):
        #    if ch not in presented:
        #        data[ch] = i
        #        presented.add(ch)
        #    elif ch in data:
        #        del data[ch]
        #return min(data.values()) if data else -1

        # code refactoring (R) - 0.08740438288077712
        data = [s.index(ch) for ch in set(s) if s.count(ch) == 1]
        return min(data) if data else -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["leetcode", "loveleetcode", "aabb", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab", "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
    t = Timer(f"for t in {query}: Solution().firstUniqChar(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

