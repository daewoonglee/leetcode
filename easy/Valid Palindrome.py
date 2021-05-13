class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 0.111923883
        # new_s = [ch.lower() for ch in s if ch.isalpha() or ch.isnumeric()]
        # for i in range(len(new_s)//2):
        #     if new_s[i] != new_s[-i-1]:
        #         return False
        # return True

        # 0.11811645900000001
        # i = 0
        # j = len(s)-1
        # while i < j:
        #     while i < j and not s[i].isalpha() and not s[i].isnumeric():
        #         i += 1
        #     while i < j and not s[j].isalpha() and not s[j].isnumeric():
        #         j -= 1
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i += 1
        #     j -= 1
        # return True

        # code refactoring 01 (R) - 0.11534614099999999
        # i = 0
        # j = len(s)-1
        # while i < j:
        #     while i < j and not s[i].isalnum():
        #         i += 1
        #     while i < j and not s[j].isalnum():
        #         j -= 1
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i += 1
        #     j -= 1
        # return True

        # code refactoring 02 (R) - 0.093488975
        new_s = "".join([c.lower() for c in s if c.isalpha() or c.isnumeric()])
        N = len(new_s)
        left = new_s[:N//2]
        right = new_s[N//2:] if N % 2 == 0 else new_s[N//2+1:]
        return left == right[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
# print(s.isPalindrome("0P"))
print(s.isPalindrome(".,"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["A man, a plan, a canal: Panama",
             "race a car",
             "0P"]
    t = Timer(f"for t in {query}: Solution().isPalindrome(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
