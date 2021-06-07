from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sorted(Counter(nums).items(), key=lambda x: x[1])[-1][0]

        log = {nums[0]: 1}
        max_num = nums[0]
        max_cnt = 1
        for n in nums[1:]:
            if n not in log:
                log[n] = 0
            log[n] += 1
            if log[n] > max_cnt:
                max_num = n
                max_cnt = log[n]
        return max_num


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
