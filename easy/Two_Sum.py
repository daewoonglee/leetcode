"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 0.04626986499999999
        # N = len(nums)
        # for i in range(N-1):
        #     for j in range(i+1, N):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # code refactoring 01: two-pass hash table
        # 0.03888810150000001
        # table = {nums[i]: i for i in range(len(nums))}
        # for i in range(len(nums)):
        #     k = target-nums[i]
        #     if k in table and table[k] != i:
        #         return [i, table[target-nums[i]]]

        # code refactoring 02: one-pass hash table
        # 0.027280625500000003
        # table = dict()
        # for i in range(len(nums)):
        #     k = target-nums[i]
        #     if k in table:
        #         return [i, table[k]]
        #     table[nums[i]] = i

        # code refactoring 02-1: one-pass hash table
        # 0.024079324
        table = dict()
        for i, n in enumerate(nums):
            k = target-n
            if k in table:
                return [i, table[k]]
            table[n] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
print(s.twoSum([-3, -4, -5, -6, -2, -1, 3, 2, 3], 6))


import timeit
avg_time = 0.
tests = [[[2, 7, 11, 15], 9],
         [[3, 2, 4], 6],
         [[3, 3], 6],
         [[-3, -4, -5, -6, -2, -1, 3, 2, 3], 6]]
for t in tests:
    avg_time += timeit.timeit(lambda: s.twoSum(*t), number=10000)
print(f'avg_time: {avg_time / len(t)}')
