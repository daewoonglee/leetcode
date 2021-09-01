class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0.035175462
        # N = len(nums)
        # nums.sort()
        # for i in range(N):
        #     if i != nums[i]:
        #         return i
        # return N

        # 0.017488182999999997
        N = len(nums)
        expected = N * (N + 1) // 2
        actual = sum(nums)
        return expected - actual


s = Solution()
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber([0, 1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[3, 0, 1],
             [9, 6, 4, 2, 3, 5, 7, 0, 1],
             [0, 1]]
    t = Timer(f"for t in {query}: Solution().missingNumber(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
