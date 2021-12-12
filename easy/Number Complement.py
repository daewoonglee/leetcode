class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #version1 - 0.28187841549515724
        #ans = ["0" if int(bn) else "1" for bn in bin(num)[2:]]
        #return int("".join(ans), 2)

        #version2 - 0.4177960129454732
        #ans = d = 0
        #while num:
        #    r = num % 2
        #    num //= 2
        #    ans+=(0 if r else 1) * 2**d
        #    d += 1
        #return ans

        # code refactoring (R) - 0.09019221644848585
        #ans = 1
        #while ans <= num:
        #    ans <<= 1
        #return (ans-1)^num

        # code refactoring (R) 02 - 0.07475931942462921
        ans = 1
        while ans <= num:
            ans *= 2
        return ans - num - 1


s = Solution()
print(s.findComplement(5))
print(s.findComplement(2))


if __name__ == '__main__':
    from timeit import Timer
    query = [5, 2, 10, 100, 1000, 10000, 2**31-1, 1, 2**20, 2**30]
    t = Timer(f"for t in {query}: Solution().findComplement(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

