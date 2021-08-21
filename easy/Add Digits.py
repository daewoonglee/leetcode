class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 0.051096737
        # while num > 9:
        #     total = 0
        #     while num:
        #         num, d = divmod(num, 10)
        #         total += d
        #     num = total
        # return num

        # code refactoring 01 - 0.051261155
        # ans = 0
        # while num:
        #     num, d = divmod(num, 10)
        #     ans += d
        #     if num == 0 and ans > 9:
        #         num = ans
        #         ans = 0
        # return ans

        # code refactoring 02 - 0.013917721
        return 1 + (num - 1) % 9 if num else 0


s = Solution()
print(s.addDigits(11))
print(s.addDigits(12))
print(s.addDigits(121))
print(s.addDigits(49))
print(s.addDigits(9999))


if __name__ == '__main__':
    from timeit import Timer
    query = [11, 12, 121, 49, 9999]
    t = Timer(f"for t in {query}: Solution().addDigits(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
