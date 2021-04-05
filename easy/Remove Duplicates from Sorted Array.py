"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.


Constraints:
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 4.4948496559999995
        # idx = 0
        # for _ in range(len(nums)-1):
        #     if nums[-1-idx] == nums[-2-idx]:
        #         nums.pop(-1-idx)
        #     else:
        #         idx += 1
        # return len(nums)

        # 3.689027874
        ans = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[ans] = nums[i+1]
                ans += 1
        return ans


s = Solution()
print(s.removeDuplicates([1, 1, 1, 2]))
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(s.removeDuplicates([1, 2, 3, 3, 3, 3]))
print(s.removeDuplicates([]))


if __name__ == '__main__':
    from timeit import Timer
    t = Timer("for t in [[1, 1, 1, 2], [1, 1, 1, 2, 2, 3], [1, 2, 3, 3, 3, 3], []]: Solution().removeDuplicates(t)", "from __main__ import Solution")
    print(t.timeit())

