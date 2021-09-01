class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 0.33316107800000005
        # N = len(nums)
        # non_zero = zero = 0
        # while N > non_zero:
        #     temp = nums[non_zero]
        #     nums[non_zero] = nums[zero]
        #     nums[zero] = temp
        #     while zero < N and nums[zero]:
        #         zero += 1
        #     non_zero = zero + 1
        #     while non_zero < N and not nums[non_zero]:
        #         non_zero += 1
        # return nums

        # code refactoring (R) 02 - 0.128687573
        non_zero = 0
        for i, n in enumerate(nums):
            if n:
                nums[i] = nums[non_zero]
                nums[non_zero] = n
                non_zero += 1
        return nums

        # code refactoring (R) 01 - 0.197359588
        # N = len(nums)
        # zero = i = 0
        # while i < N - zero:
        #     if not nums[i]:
        #         nums.pop(i)
        #         zero += 1
        #     else:
        #         i += 1
        # for _ in range(zero):
        #     nums.append(0)
        # return nums


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
print(s.moveZeroes([0, 0, 1, 3, 12]))
print(s.moveZeroes([1, 3, 12, 0, 0]))
print(s.moveZeroes([1, 0, 0, 2, 0]))
print(s.moveZeroes([1, 2, 0, 3, 0]))
print(s.moveZeroes([1]))
print(s.moveZeroes([1, 2, 3, 4, 5]))
print(s.moveZeroes([0, 0, 0, 0, 0]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[0, 1, 0, 3, 12],
             [0, 0, 1, 3, 12],
             [1, 3, 12, 0, 0],
             [1, 0, 0, 2, 0],
             [1, 2, 0, 3, 0],
             [1],
             [1, 2, 3, 4, 5],
             [0, 0, 0, 0, 0],
             [0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0]]
    t = Timer(f"for t in {query}: Solution().moveZeroes(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
