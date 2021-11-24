class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # version1
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
        
        # version2
        return list(set(i for i in range(1, len(nums)+1)) - set(nums))

       
s = Solution()
print(s.findDisappearedNumbers([1,2,3,4,5]))
print(s.findDisappearedNumbers([1,1,1,1,5]))
print(s.findDisappearedNumbers([1,1]))
        
