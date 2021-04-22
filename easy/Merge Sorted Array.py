"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 0.220762756
        # i = 0
        # j = 0
        # while j < n and i-j < m:
        #     if nums1[i] > nums2[j]:
        #         for z in range(m+j, i, -1):
        #             nums1[z] = nums1[z-1]
        #         nums1[i] = nums2[j]
        #         j += 1
        #     i += 1
        # for z in range(n-j):
        #     nums1[i+z] = nums2[j+z]
        # return nums1

        # code refactoring - 0.16755922699999998
        i = m-1
        j = n-1
        z = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[z] = nums2[j]
                j -= 1
            else:
                nums1[z] = nums1[i]
                i -= 1
            z -= 1
        for k in range(j+1):
            nums1[k] = nums2[k]
        return nums1


s = Solution()
# print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(s.merge([1, 1, 1, 1, 0], 4, [2], 1))
# print(s.merge([2, 3, 4, 5, 0], 4, [1], 1))
# print(s.merge([1], 1, [], 0))
# print(s.merge([0], 0, [1], 1))
print(s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
print(s.merge([-1, 0, 0, 2, 2, 3, 0, 0, 0], 6, [1, 2, 2], 3))
print(s.merge([1, 2, 3, 0, 0, 0, 0], 3, [2, 5, 6, 7], 4))
print(s.merge([-1, 0, 1, 1, 0, 0, 0, 0, 0], 4, [-1, 0, 2, 2, 3], 5))
print(s.merge([-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 5, [-1, -1, 0, 0, 1, 2], 6))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
             [[1, 1, 1, 1, 0], 4, [2], 1],
             [[2, 3, 4, 5, 0], 4, [1], 1],
             [[1], 1, [], 0],
             [[0], 0, [1], 1],
             [[4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3],
             [[-1, 0, 0, 2, 2, 3, 0, 0, 0], 6, [1, 2, 2], 3],
             [[1, 2, 3, 0, 0, 0, 0], 3, [2, 5, 6, 7], 4],
             [[-1, 0, 1, 1, 0, 0, 0, 0, 0], 4, [-1, 0, 2, 2, 3], 5],
             [[-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 5, [-1, -1, 0, 0, 1, 2], 6]]
    t = Timer(f"for t in {query}: Solution().merge(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
