class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Limit Exceeded
        # N = len(numbers)
        # for i, n in enumerate(numbers[:-1]):
        #     num = target - n
        #     for j in range(i+1, N):
        #         if num == numbers[j]:
        #             return [i+1, j+1]

        N = len(numbers)
        for i in range(N//2+1):
            num = target - numbers[i]
            L = i
            pivot = N//2
            R = N-1
            while L <= R:
                print(f"pivot: {pivot}")
                pn = numbers[pivot]
                if num < pn:
                    R = pivot-1
                    pivot = (R+L)//2+1
                elif num > pn:
                    L = pivot+1
                    pivot = (R+L)//2
                else:
                    return [i+1, pivot+1]


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))      # [1,2]
# print(s.twoSum([2, 3, 4], 6))           # [1,3]

# print(s.twoSum([5, 5], 10))             # [1,2]
# print(s.twoSum([-1, 0], -1))            # [1,2]
# print(s.twoSum([-5, -5, -1, 0], -10))   # [1,2]

# print(s.twoSum([-3, 3, 4, 90], 0))      # [1,2]
# print(s.twoSum([5, 25, 75], 100))      # [2,3]
print(s.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # [4, 5]
