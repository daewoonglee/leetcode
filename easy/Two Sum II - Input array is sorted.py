class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 0.12534178699999998
        # N = len(numbers)
        # for i in range(N-1):
        #     num = target - numbers[i]
        #     L = i+1
        #     R = N-1
        #     while L <= R:
        #         pivot = (R+L)//2
        #         pn = numbers[pivot]
        #         # print(f"pivot: {pivot}, pn: {pn}")
        #         if num < pn:
        #             R = pivot-1
        #         elif num > pn:
        #             L = pivot+1
        #         else:
        #             return [i+1, pivot+1]

        # code refactoring 01 - 0.084737223
        # L = 0
        # R = len(numbers)-1
        # while L <= R:
        #     n = numbers[L] + numbers[R]
        #     if n < target:
        #         L += 1
        #     elif n > target:
        #         R -= 1
        #     else:
        #         return [L+1, R+1]

        # code refactoring 02 - 0.101679039
        logs = {}
        for i, n in enumerate(numbers):
            if n in logs:
                return [logs[n]+1, i+1]
            logs[target - n] = i


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))      # [1,2]
# print(s.twoSum([2, 3, 4], 6))           # [1,3]

# print(s.twoSum([5, 5], 10))             # [1,2]
# print(s.twoSum([-1, 0], -1))            # [1,2]
# print(s.twoSum([-5, -5, -1, 0], -10))   # [1,2]

print(s.twoSum([-3, 3, 4, 90], 0))      # [1,2]
# print(s.twoSum([5, 25, 75], 100))       # [2,3]
# print(s.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # [4, 5]


if __name__ == '__main__':
    from timeit import Timer
    query = [[[2, 7, 11, 15], 9],
             [[2, 3, 4], 6],
             [[5, 5], 10],
             [[-1, 0], -1],
             [[-5, -5, -1, 0], -10],
             [[-3, 3, 4, 90], 0],
             [[5, 25, 75], 100],
             [[1, 2, 3, 4, 4, 9, 56, 90], 8],
             [[1, 2, 3, 4, 4, 5, 6, 7], 8]]
    t = Timer(f"for t in {query}: Solution().twoSum(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
