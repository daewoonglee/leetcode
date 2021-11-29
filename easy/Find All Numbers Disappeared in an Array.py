class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # version1 - 1.7308185854926705
        #N = len(nums)
        #nums = sorted(set(nums))
        #ans = []
        #j = 0
        #for i in range(1, N+1):
        #    if j>=len(nums) or i != nums[j]:
        #        ans.append(i)
        #    else:
        #        j+=1
        #return ans
        
        # version2 - 0.9007303398102522
        #return list(set(i for i in range(1, len(nums)+1)) - set(nums))

        # code refactoring (R) - 1.1984849069267511
        flags = [1 for _ in nums]
        for n in nums:
            flags[n-1] = 0
        return [i+1 for i, flag in enumerate(flags) if flag]

  
s = Solution()
print(s.findDisappearedNumbers([1,2,3,4,5]))
print(s.findDisappearedNumbers([1,1,1,1,5]))
print(s.findDisappearedNumbers([1,1]))
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1,2,3,4,5], [1,1,1,1,5], [1,1], [4,3,2,7,8,2,3,1], [i+1 for i in range(1000)],[3, 5, *[1 for _ in range(100)], 10]]
    t = Timer(f"for t in {query}: Solution().findDisappearedNumbers(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
        
