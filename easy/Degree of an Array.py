from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        N = len(nums)
        subarray = {n: [-1, N] for n in nums}
        for i, n in enumerate(nums):
            idx = 0 if subarray[n][0] == -1 else 1
            subarray[n][idx] = i

        ans = N
        count_dict = sorted(Counter(nums).items(), key=lambda x: x[1])[::-1]
        max_count = count_dict[0][1]
        if max_count == 1: return 1
        for k, v in count_dict:
            if v != max_count:
                break
            start_idx, end_idx = subarray[k]
            ans = ans if ans < (end_idx - start_idx + 1) else (end_idx - start_idx + 1)
        return ans


s = Solution()
# print(s.findShortestSubArray([1,2,2,3,1])) # 2
# print(s.findShortestSubArray([1,2,2,3,1,4,2])) # 6
# print(s.findShortestSubArray([0])) # 1
print(s.findShortestSubArray([0,1,2,1,1,2,0,0,2])) # 4
