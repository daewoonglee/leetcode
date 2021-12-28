class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        start, end = ord("A"), ord("Z")
        res = [1 if start <= ord(ch) <= end else 0 for ch in word]
        res_sum = sum(res)
        return not res_sum or res_sum == len(word) or (res_sum == 1 and res[0] == 1)


s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("UUa"))
print(s.detectCapitalUse("U"))
print(s.detectCapitalUse("Usa"))
print(s.detectCapitalUse("usa"))
print(s.detectCapitalUse("u"))

