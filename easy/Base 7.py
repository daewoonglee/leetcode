class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 0.10429806262254715
        #sign = False
        #if num < 0:
        #    num *= -1
        #    sign = True
        #
        #base7 = []
        #while num >= 1:
        #    d = num%7
        #    num //= 7
        #    base7.append(str(d))
        #ans = "".join(base7[::-1]) if base7 else "0"
        #return ans if not sign else "-" + ans

        # code refactoring - 0.0871276231482625
        #sign = False
        #if num < 0:
        #    num *= -1
        #    sign = True
        #
        #ans = ""
        #while num >= 1:
        #    ans += str(num % 7)
        #    num //= 7
        #return "-" + ans if sign else ans

        # code refactoring (R) - 0.09958688076585531
        if num < 0:
            return '-' + self.convertToBase7(-num)
        elif num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)


s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-7))
print(s.convertToBase7(777))
print(s.convertToBase7(0))
print(s.convertToBase7(-1))


if __name__ == '__main__':
    from timeit import Timer
    query = [100, -7,  777, 0, -1, 10000000, -10000000]
    t = Timer(f"for t in {query}: Solution().convertToBase7(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

