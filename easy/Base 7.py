class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        sign = False
        if num < 0:
            num *= -1
            sign = True

        base7 = []
        while num >= 1:
            d = num%7
            num //= 7
            base7.append(str(d))
        ans = "".join(base7[::-1]) if base7 else "0"
        return ans if not sign else "-" + ans
 

s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-7))
print(s.convertToBase7(777))
print(s.convertToBase7(0))
print(s.convertToBase7(-1))

