from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0.163955278
        # return sorted(Counter(nums).items(), key=lambda x: x[1])[-1][0]

        # 0.077528243
        # log = {nums[0]: 1}
        # max_num = nums[0]
        # max_cnt = 1
        # for n in nums[1:]:
        #     if n not in log:
        #         log[n] = 0
        #     log[n] += 1
        #     if log[n] > max_cnt:
        #         max_num = n
        #         max_cnt = log[n]
        # return max_num

        # code refactoring (R) 01 - 0.061775794999999994
        # cnt = {}
        # N = len(nums)//2
        # for n in nums:
        #     if n not in cnt:
        #         cnt[n] = nums.count(n)
        #         if cnt[n] > N:
        #             return n

        # code refactoring (R) 02 - 0.04522256499999999
        # count = 0
        # majority = nums[0]
        # for num in nums:
        #     if count == 0:
        #         majority = num
        #     if majority == num:
        #         count += 1
        #     else:
        #         count -= 1
        # return majority

        # code refactoring (R) 03 - 0.024781176
        nums.sort()
        return nums[len(nums)//2]


s = Solution()
# print(s.majorityElement([3, 2, 3]))
# print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([1, 2, 3, 2, 3, 3, 3]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[3, 2, 3],
             [2, 2, 1, 1, 1, 2, 2],
             [1, 2, 3, 2, 3, 3, 3],
             [7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]]
    t = Timer(f"for t in {query}: Solution().majorityElement(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
