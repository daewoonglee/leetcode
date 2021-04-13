"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 0.0953646
        # return list(str(int("".join(map(str, digits)))+1))

        # code refactoring 01 - 0.030296527000000004
        # idx = len(digits)-1
        # while idx >= 0:
        #     if digits[idx] < 9:
        #         digits[idx] += 1
        #         return digits
        #     else:
        #         digits[idx] = 0
        #         idx -= 1
        # if digits[0] == 0:
        #     # digits.insert(0, 1)
        #     digits = [1] + digits
        # return digits

        # code refactoring 02 - 0.130047577
        d = 0
        N = len(digits)-1
        for i, n in enumerate(digits):
            d += (n * 10**(N-i))
        d += 1
        return [int(num) for num in str(d)]


s = Solution()
# print(s.plusOne([1, 2, 3]))
# print(s.plusOne([4, 3, 2, 1]))
# print(s.plusOne([0]))
# print(s.plusOne([9]))
# print(s.plusOne([9, 9])) # [1, 0, 0]
print(s.plusOne([9, 9, 0, 9])) # [1, 0, 0]
print(s.plusOne([9, 9, 9, 9])) # [1, 0, 0]


if __name__ == '__main__':
    from timeit import Timer
    query = [[1, 2, 3], [4, 3, 2, 1], [0], [9], [9, 9]]
    t = Timer(f"for t in {query}: Solution().plusOne(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
