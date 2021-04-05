


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for _ in range(len(nums)-1):
            # print(f"idx: {idx}")
            if nums[-1-idx] == nums[-2-idx]:
                nums.pop(-1-idx)
            else:
                idx += 1
        # print(nums)
        return len(nums)


s = Solution()
print(s.removeDuplicates([1, 1, 1, 2]))
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(s.removeDuplicates([1, 2, 3, 3, 3, 3]))
