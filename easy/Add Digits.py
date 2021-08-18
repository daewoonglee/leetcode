class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            q, d = -1, -1
            total = 0
            while q:
                q, d = divmod(num, 10)
                total += d
                num = q
            num = total
        return num


s = Solution()
print(s.addDigits(11))
print(s.addDigits(12))
print(s.addDigits(121))
print(s.addDigits(49))
