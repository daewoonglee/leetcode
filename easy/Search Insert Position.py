"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 3.958087464
        # for i in range(len(nums)):
        #     if nums[i] >= target or nums[i] > target:
        #         return i
        # return len(nums)

        # code refactoring 01 - 3.5671307729999997
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        # return len(nums)

        # code refactoring 02 - 3.66879623
        l = 0
        r = len(nums)
        while l < r:
            pivot = (r - l) // 2 + l
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                l = pivot+1
            else:
                r = pivot
        return l


s = Solution()
# print(s.searchInsert([1, 3, 5, 6], 5))    # 2
# print(s.searchInsert([1, 3, 5, 6], 2))    # 1
# print(s.searchInsert([1, 3, 5, 6], 7))    # 4
# print(s.searchInsert([1, 3, 5, 6], 0))    # 0
# print(s.searchInsert([1], 0))             # 0
print(s.searchInsert([1, 3], 2))          # 1


if __name__ == '__main__':
    from timeit import Timer
    t = Timer("for t in [[[1, 3, 5, 6], 5], [[1, 3, 5, 6], 2], [[1, 3, 5, 6], 7], [[1, 3, 5, 6], 0], [[1], 0]]: Solution().searchInsert(*t)",
              "from __main__ import Solution")
    print(t.timeit())
