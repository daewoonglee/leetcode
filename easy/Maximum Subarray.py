"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        ans = nums[0]
        for i in range(N):
            n = nums[i]
            if ans < n:
                ans = n
            for j in range(i+1, N, 1):
                n += nums[j]
                if ans < n:
                    ans = n
        return ans


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
# print(s.maxSubArray([1]))                               # 1
# print(s.maxSubArray([5, 4, -1, 7, 8]))                  # 23
# print(s.maxSubArray([-1, -1, -1, -1, 1]))               # 1
print(s.maxSubArray([-1]))                              # -1
# print(s.maxSubArray([-1, 0, -2]))                       # 0


if __name__ == '__main__':
    from timeit import Timer
    t = Timer("for t in [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8], [-1, -1, -1, -1, 1], [-1], [-1, 0, 2]]"
              ": Solution().maxSubArray(t)", "from __main__ import Solution")
    print(t.timeit())
