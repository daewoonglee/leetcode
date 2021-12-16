class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # 34.93233369477093
        #nums = [1] + [d for d in range(2, area // 2 + 1) if area % d == 0] + [area]
        #p = len(nums) // 2
        #return [nums[p], nums[p]] if len(nums) % 2 == 1 else [nums[p], nums[p-1]]

        # code refactoring - 0.06923562660813332
        # 효율적인 약수 이론 방법 참고 
        #d = int(area**0.5)
        #while d > 1 and area % d != 0:
        #    d -= 1
        #return [area//d, d]

        # code refactoring (R) - 0.056474752724170685
        for d in range(int(area**0.5), 1, -1):
            if area % d == 0:
                return [area//d, d]
        return [area, 1]

s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(37))
print(s.constructRectangle(122122))
print(s.constructRectangle(3))


if __name__ == '__main__':
    from timeit import Timer
    query = [4, 37, 122122]
    t = Timer(f"for t in {query}: Solution().constructRectangle(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

