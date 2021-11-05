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
        cnts = [0, 0]
        for r in range(turnedOn+1):
            for comb_h in list(combinations(H, r)):
                comb_h_s = sum(comb_h)
                cnts[0] += 1
                if comb_h_s > 11:
                    continue
                for comb_m in list(combinations(M, turnedOn - r)):
                    comb_m_s = sum(comb_m)
                    cnts[1] += 1
                    if comb_m_s > 59:
                        continue
                    ans.append(f"{comb_h_s}:{comb_m_s:02}")
        print(f"turnedOn: {turnedOn}, cnt: {sum(cnts)}")
        '''
        turnedOn: 0, cnt: 2
        turnedOn: 1, cnt: 15
        turnedOn: 2, cnt: 55
        turnedOn: 3, cnt: 127
        turnedOn: 4, cnt: 198
        turnedOn: 5, cnt: 212
        turnedOn: 6, cnt: 156
        turnedOn: 7, cnt: 80
        turnedOn: 8, cnt: 33
        '''
        return ans

        # code refactoring (R) 01 - 2.5970965307205915 (매번 720번을 돌아서 느림)
        #rList = []
        #cnt = 0
        #for h in range(12):
        #    for m in range(60):
        #        if (bin(h) + bin(m)).count('1') == turnedOn:
        #            rList.append("{}:{:0>2d}".format(h,m))
        #        cnt += 1
        #print(f"turnedOn: {turnedOn}, cnt: {cnt}")
        #return rList
        '''
        turnedOn: 0, cnt: 720
        turnedOn: 1, cnt: 720
        turnedOn: 2, cnt: 720
        turnedOn: 3, cnt: 720
        turnedOn: 4, cnt: 720
        turnedOn: 5, cnt: 720
        turnedOn: 6, cnt: 720
        turnedOn: 7, cnt: 720
        turnedOn: 8, cnt: 720
        '''

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
    #print(t.timeit(number=1000))
    print(t.timeit(number=1))
