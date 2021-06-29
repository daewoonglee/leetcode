class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = set()
        while n != 1:
            n = sum([int(n1)**2 for n1 in list(str(n))])
            if n in cycle:
                return False
            cycle.add(n)
        return True


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
