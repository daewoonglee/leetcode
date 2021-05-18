class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0.04456803299999999
        # nums.sort()
        # for i in range(0, len(nums)-1, 2):
        #     if nums[i] != nums[i+1]:
        #         return nums[i]
        # return nums[-1]

        # code refactoring 01 - 0.039722647
        # return sum(set(nums)) * 2 - sum(nums)

        # code refactoring 02 - 0.026619917999999996
        ans = 0
        for n in nums:
            ans ^= n
        return ans


s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([1]))
print(s.singleNumber([4, 1, 2, 1, 2]))
print(s.singleNumber([1, 2, 3, 4, 5, 4, 3, 2, 1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[2, 2, 1],
             [1],
             [4, 1, 2, 1, 2],
             [1, 2, 3, 4, 5, 4, 3, 2, 1]]
    t = Timer(f"for t in {query}: Solution().singleNumber(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
