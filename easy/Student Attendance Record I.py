class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #version 1
        #return False if s.count("A") >= 2 or s.find("LLL") != -1 else True

        #version 2
        log = {k: 0 for k in "ALP"}
        for i, ch in enumerate(s[:-2]):
            log[ch] += 1
            if (ch == "A" and log[ch] >= 2) or ch=="L" and s[i:i+3] == "LLL": return False
        return False if log["A"] + s[-2:].count("A") >= 2 else True

s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
print(s.checkRecord("L"))
print(s.checkRecord("LLPLLALLA"))

