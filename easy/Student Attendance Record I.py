class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #version 1 - 0.02815915457904339
        #return False if s.count("A") >= 2 or s.find("LLL") != -1 else True

        #version 2 - 0.31037546321749687
        #log = {k: 0 for k in "ALP"}
        #for i, ch in enumerate(s[:-2]):
        #    log[ch] += 1
        #    if (ch == "A" and log[ch] >= 2) or ch=="L" and s[i:i+3] == "LLL": return False
        #return False if log["A"] + s[-2:].count("A") >= 2 else True

        # code refactoring - 0.15053368173539639
        """
        a_cnt = 0
        for ch in s:
            if ch == "A": 
                a_cnt+= 1
                if a_cnt == 2: return False

        l_idx = -2
        for i, ch in enumerate(s[:-2]):
            if ch == "L":
                if l_idx + 1 < i:
                    l_idx = i
                    if s[i: i+3] == "LLL": return False
        return True
        """

        # code refactoring (R) - 0.1464805882424116
        a_cnt = 0
        l_cnt = 0
        for ch in s:
            if ch == "A": 
                a_cnt += 1
                l_cnt = 0
                if a_cnt == 2: return False
            elif ch == "L": 
                l_cnt += 1
                if l_cnt == 3: return False
            else: l_cnt = 0
        return True


s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
print(s.checkRecord("L"))
print(s.checkRecord("LLPLLALLA"))
print(s.checkRecord("PLLPLLLLPP"))
print(s.checkRecord("LPPLPLLLPLPP"))

if __name__ == '__main__':
    from timeit import Timer
    query = ["PPALLP", "PPALLL", "L", "LLPLLALLA", "PLLPLLLLPP", "P"*100+"LLL", "A"+"P"*100+"A"]
    t = Timer(f"for t in {query}: Solution().checkRecord(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

