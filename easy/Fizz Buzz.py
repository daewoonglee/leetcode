class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            # 3.548612317070365
            #if i % 15 == 0: ans.append("FizzBuzz")
            #elif i % 3 == 0: ans.append("Fizz")
            #elif i % 5 == 0: ans.append("Buzz")
            #else: ans.append(str(i))

            # code refactoring (R) - 3.2298794900998473 
            ans_str = "Fizz" if i % 3 == 0 else ""
            ans_str += "Buzz" if i % 5 == 0 else ""
            ans.append(ans_str if ans_str else str(i))
        return ans


s = Solution()
print(s.fizzBuzz(15))
print(s.fizzBuzz(3))
print(s.fizzBuzz(5))
print(s.fizzBuzz(12))


if __name__ == '__main__':
    from timeit import Timer
    query = [15, 3, 5, 12, 100, 1000, 10000, 1]
    t = Timer(f"for t in {query}: Solution().fizzBuzz(t)", "from __main__ import Solution")
    print(t.timeit(number=1000))

