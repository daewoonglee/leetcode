class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        # 0.413693682
        # N = len(nums)-1
        # global_start_num = 0
        # flag = False
        # ans = []
        # i = 0
        # while i < N:
        #     start_num = nums[i]
        #     next_num = nums[i+1]
        #     i += 1
        #     if start_num + 1 == next_num:
        #         if not flag:
        #             global_start_num = start_num
        #             flag = True
        #         continue
        #     else:
        #         if flag:
        #             ans.append(f"{global_start_num}->{start_num}")
        #         else:
        #             ans.append(str(start_num))
        #         flag = False
        # ans.append(f"{global_start_num}->{nums[-1]}" if flag else str(nums[-1]))
        # return ans

        # code refactoring - 0.401652945
        # N = len(nums)-1
        # ans = []
        # global_i = -1
        # i = 0
        # while i < N:
        #     if nums[i]+1 == nums[i+1]:
        #         if global_i == -1:
        #             global_i = i
        #     else:
        #         ans.append(f"{nums[global_i]}->{nums[i]}" if global_i != -1 else str(nums[i]))
        #         global_i = -1
        #     i += 1
        # ans.append(f"{nums[global_i]}->{nums[-1]}" if global_i != -1 else str(nums[-1]))
        # return ans

        # code refactoring (R) - 0.360510544
        ans = []
        pointer = 0
        for i, n in enumerate(nums[:-1]):
            if n+1 != nums[i+1]:
                ans.append(f"{nums[pointer]}->{n}" if nums[pointer] != n else str(n))
                pointer = i+1
        ans.append(f"{nums[pointer]}->{nums[-1]}" if nums[pointer] != nums[-1] else str(nums[-1]))
        return ans


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
print(s.summaryRanges([]))
print(s.summaryRanges([-1]))
print(s.summaryRanges([0]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[0, 1, 2, 4, 5, 7],
             [0, 2, 3, 4, 6, 8, 9],
             [],
             [-1],
             [0],
             list(range(100)),
             list(range(0, 100, 2))]
    t = Timer(f"for t in {query}: Solution().summaryRanges(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
