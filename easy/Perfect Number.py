class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        total_num = 1
        for n in range(2, int(num**0.5)+1, 1):
            if num % n == 0:
                total_num += n
                total_num += num//n
        return total_num == num and num != 1


s = Solution()
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(27))
print(s.checkPerfectNumber(1))
 
