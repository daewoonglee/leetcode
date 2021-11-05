from itertools import combinations

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        # 0.46985187008976936
        if turnedOn in [9, 10]:
            return []

        H = [8, 4, 2, 1]
        M = [32, 16, 8, 4, 2, 1]
        ans = []
        for r in range(turnedOn+1):
            for comb_h in list(combinations(H, r)):
                comb_h_s = sum(comb_h)
                if comb_h_s > 11:
                    continue
                for comb_m in list(combinations(M, turnedOn - r)):
                    comb_m_s = sum(comb_m)
                    if comb_m_s > 59:
                        continue
                    ans.append(f"{comb_h_s}:{comb_m_s:02}")
        return ans

        # code refactoring (R) 01 - 2.5970965307205915
        #rList = []
        #for h in range(12):
        #    for m in range(60):
        #        if (bin(h) + bin(m)).count('1') == turnedOn:
        #            rList.append("{}:{:0>2d}".format(h,m))
        #return rList


s = Solution()
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))
#print(s.readBinaryWatch(0))
#print(s.readBinaryWatch(9))
#print(s.readBinaryWatch(8))


if __name__ == '__main__':
    from timeit import Timer
    query = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = Timer(f"for t in {query}: Solution().readBinaryWatch(t)", "from __main__ import Solution")
    print(t.timeit(number=1000))

