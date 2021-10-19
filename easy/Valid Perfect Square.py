class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 0.02266033599153161
        # return (num ** 0.5) % 2 in [0, 1]

        # code refactoring - 0.019051427952945232        
        # return (num ** 0.5).is_integer()

        # code refactoring (R) - 0.02775065414607525
        if num < 2:
            return True
        
        left = 2
        right = num / 2
        
        while left <= right:
            pivot = (left + right) / 2
            
            temp = pivot * pivot
            
            if temp < num:
                left = pivot + 1
            elif temp > num:
                right = pivot - 1
            else:
                return True
            
        return False

s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
print(s.isPerfectSquare(1))
print(s.isPerfectSquare(2))
print(s.isPerfectSquare(3))
print(s.isPerfectSquare(9))


if __name__ == '__main__':
    from timeit import Timer
    query = [16, 14, 1, 2, 3, 9]
    t = Timer(f"for t in {query}: Solution().isPerfectSquare(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

