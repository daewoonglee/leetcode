class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 0.017453459091484547
        #return len(s.split())

        # without built-in function - 0.05456833727657795
        #if s == "":
        #    return 0
        #cnt = 0
        #for i, ch in enumerate(s[:-1]):
        #    if ch == " " and s[i+1] != " ":
        #        cnt += 1
        #return cnt if s[0] == " " else cnt + 1

        # without built-in function code refactoring (R) - 0.04684274364262819
        if not len(s):
            return 0
        count = 0
        is_blank = True
        for ch in s:
            if not ch == " " and is_blank:
                count += 1
                is_blank = False
            elif ch == " ":
                is_blank = True
        return count


s = Solution()
print(s.countSegments("Hello, my name is John"))
print(s.countSegments("Hello"))
print(s.countSegments("love live! mu'sic forever"))
print(s.countSegments(""))
print(s.countSegments("   G iii"))
print(s.countSegments("   G      "))


if __name__ == '__main__':
    from timeit import Timer
    query = ["Hello, my name is John", "Hello", "love live! mu'sic forever", "", "    for iiii"]
    t = Timer(f"for t in {query}: Solution().countSegments(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
        
