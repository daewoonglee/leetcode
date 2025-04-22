from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        N = len(nums)
        count_dict = sorted(Counter(nums).items(), key=lambda x: x[1])[::-1]
        max_count = count_dict[0][1]
        max_dict = {}
        for k, v in count_dict:
            if v != max_count:
                break
            max_dict[k] = [0, N-1]

        ans = N
        for k, (start_idx, end_idx) in max_dict.items():
            while start_idx < end_idx:
                if nums[start_idx] == k:
                    break
                start_idx += 1
            while start_idx < end_idx:
                if nums[end_idx] == k:
                    break
                end_idx -= 1
            ans = ans if ans < (end_idx - start_idx + 1) else (end_idx - start_idx + 1)
        return ans


s = Solution()
# print(s.findShortestSubArray([1,2,2,3,1])) # 2
# print(s.findShortestSubArray([1,2,2,3,1,4,2])) # 6
# print(s.findShortestSubArray([0])) # 1
print(s.findShortestSubArray([0,1,2,1,1,2,0,0,2])) # 4
