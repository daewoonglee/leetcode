class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        subarray = {n: [] for n in nums}
        for i, n in enumerate(nums):
            subarray[n].append(i)
        max_count = max([len(arr) for arr in subarray.values()])
        return min([arr[-1] - arr[0] for arr in subarray.values() if len(arr) == max_count]) + 1


s = Solution()
# print(s.findShortestSubArray([1,2,2,3,1])) # 2
# print(s.findShortestSubArray([1,2,2,3,1,4,2])) # 6
# print(s.findShortestSubArray([0])) # 1
print(s.findShortestSubArray([0,1,2,1,1,2,0,0,2])) # 4
