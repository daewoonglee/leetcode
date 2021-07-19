class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        N = len(nums)-1
        global_start_num = 0
        flag = False
        ans = []
        i = 0
        while i < N:
            start_num = nums[i]
            next_num = nums[i+1]
            i += 1
            if start_num + 1 == next_num:
                if not flag:
                    global_start_num = start_num
                    flag = True
                continue
            else:
                if flag:
                    ans.append(f"{global_start_num}->{start_num}")
                else:
                    ans.append(str(start_num))
                flag = False
        ans.append(f"{global_start_num}->{nums[-1]}" if flag else str(nums[-1]))
        return ans


s = Solution()
# print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
# print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
print(s.summaryRanges([]))
print(s.summaryRanges([-1]))
print(s.summaryRanges([0]))
