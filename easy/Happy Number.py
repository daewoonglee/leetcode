class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 0.5041988110000001
        # cycle = set()
        # while n != 1:
        #     n = sum([int(n1)**2 for n1 in list(str(n))])
        #     if n in cycle:
        #         return False
        #     cycle.add(n)
        # return True

        # code refactoring 01 - 0.472717931
        # cycle = list()
        # while n != 1:
        #     n = sum([int(n1)**2 for n1 in list(str(n))])
        #     if n in cycle:
        #         return False
        #     cycle.append(n)
        # return True

        # code refactoring (R) 01 - 0.215242408
        # while n != 1:
        #     if n in [2, 3, 4]:
        #         return False
        #     total = 0
        #     for i in list(str(n)):
        #         total += int(i) ** 2
        #     n = total
        # return True

        # code refactoring (R) 02 - 0.06751570800000001
        r = 0
        # 1, 7을 제외한 10이하 수가 나오면 실패이기 때문에 //10 조건문으로 루프 탈출
        # 위 cycle을 생성하는지 확인할 필요가 없음
        while n//10 != 0:
            new = 0
            x = n
            while x != 0:
                r = x % 10
                new += (r * r)
                x //= 10
            n = new
        return n == 1 or n == 7 # 0~9 사이에선 1이랑 7이 조건 만족


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
print(s.isHappy(7))


if __name__ == '__main__':
    from timeit import Timer
    query = [19,
             2,
             22222,
             12345667]
    t = Timer(f"for t in {query}: Solution().isHappy(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
