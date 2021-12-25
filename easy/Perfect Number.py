class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 0.6645889421924949
        #total_num = 1
        #for n in range(2, int(num**0.5)+1, 1):
        #    if num % n == 0:
        #        total_num += n
        #        total_num += num//n
        #return total_num == num and num != 1

        # code refactoring - 0.7703832117840648
        #total_num = 1
        #for n in range(2, int(num**0.5)+1):
        #    if num % n == 0:
        #        total_num += n
        #        if n ** 2 != num: 
        #            total_num += num//n
        #return total_num == num and num != 1

        # code refactoring (R) - 0.20347778033465147
        total_num = 1
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                total_num += n
                if n ** 2 != num:
                    total_num += num//n
                if total_num > num: return False
        return total_num == num and num != 1


s = Solution()
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(27))
print(s.checkPerfectNumber(1))
print(s.checkPerfectNumber(16))


if __name__ == '__main__':
    from timeit import Timer
    query = [28, 27, 1, 1000, 10000, 999999]
    t = Timer(f"for t in {query}: Solution().checkPerfectNumber(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

