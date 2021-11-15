class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0.04552824702113867
        #sort_nums = sorted(set(nums), reverse=True)
        #return sort_nums[2] if len(sort_nums) > 2 else sort_nums[0]

        # 0.04395189927890897
        set_nums = set(nums)
        return max(set_nums) if len(set_nums) < 3 else sorted(set_nums, reverse=True)[2]


s = Solution()
print(s.thirdMax([1,1,3,2,0]))
print(s.thirdMax([1,1,1,1,1,1,1,1,1,3]))
print(s.thirdMax([1,2]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1,1,3,2,0], [1,1,1,1,1,1,1,1,1,3], [1,2,3,4,5,6,7,8,9,0], [-1,-2,-3,-0,1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16,17]]
    t = Timer(f"for t in {query}: Solution().thirdMax(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
 
