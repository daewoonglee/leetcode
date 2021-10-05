class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))


s = Solution()
print(s.intersection([1,2,2,1], nums2=[2,2]))
print(s.intersection([4,9,5], nums2=[9,4,9,8,4]))

