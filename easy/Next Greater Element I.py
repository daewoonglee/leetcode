class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for n1 in nums1:
            # find index
            #idx = 0
            #for i, n2 in enumerate(nums2):
            #    if n1 == n2:
            #        idx = i
            #        break
            idx = nums2.index(n1)
            n = nums2[idx]
            flag = False
            for i, n2 in enumerate(nums2[idx+1:]):
                if n < n2:
                    ans.append(n2)
                    flag=True
                    break
            if not flag:
                ans.append(-1)
        return ans
                        

s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
print(s.nextGreaterElement([4,1,2], [1,2,0,4]))

