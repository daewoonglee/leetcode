class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 0.5026397472247481
        #start, end = ord("A"), ord("Z")
        #res = [1 if start <= ord(ch) <= end else 0 for ch in word]
        #res_sum = sum(res)
        #return not res_sum or res_sum == len(word) or (res_sum == 1 and res[0] == 1)

        # code refactoring - 0.24399275425821543
        #if len(word) == 1: return True
        #upper_start, upper_end = ord("A"), ord("Z")
        #lower_start, lower_end = ord("a"), ord("z")
        #if upper_start <= ord(word[0]) <= upper_end:
        #    start, end = (upper_start, upper_end) if upper_start <= ord(word[1]) <= upper_end else (lower_start, lower_end)
        #    for ch in word[2:]:
        #        if not start <= ord(ch) <= end: return False
        #    return True
        #else:
        #    for ch in word[1:]:
        #        if not lower_start <= ord(ch) <= lower_end: return False
        #    return True

        # code refactoring (R) - 0.029775178991258144
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())


s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("UUa"))
print(s.detectCapitalUse("U"))
print(s.detectCapitalUse("Usa"))
print(s.detectCapitalUse("usa"))
print(s.detectCapitalUse("u"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["u"*100, "usa"*30, "Usa"*30, "USa"*30, "USA"*30]
    t = Timer(f"for t in {query}: Solution().detectCapitalUse(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

