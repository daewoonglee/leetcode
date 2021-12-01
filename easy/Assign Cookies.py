class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 2.885856855660677
        #g.sort()
        #s.sort()
        #ans = i = j = 0
        #while i < len(g) and j < len(s):
        #    if s[j] >= g[i]:
        #        ans += 1
        #        i += 1
        #    j += 1
        #return ans

        # code refactoring - 0.9900464471429586
        g.sort()
        s.sort()
        N = len(g)
        i = 0
        for n in s:
            if n >= g[i]:
                i += 1
                if i >= N:
                    break
        return i


s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))
print(s.findContentChildren([1,2,3], [3]))
print(s.findContentChildren([1,2,3], [2,3]))
print(s.findContentChildren([1,1,1], [2,3,4]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[1,2,3], [1,1]], [[1,2,3], [3]], [[1,2,3], [2,3]], [[1,1,1], [2,3,4]], [[i+1 for i in range(1000)], [i+1 for i in range(1000)]]]
    t = Timer(f"for t in {query}: Solution().findContentChildren(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

