from itertools import combinations

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
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


s = Solution()
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))
print(s.readBinaryWatch(0))
print(s.readBinaryWatch(9))
print(s.readBinaryWatch(8))

