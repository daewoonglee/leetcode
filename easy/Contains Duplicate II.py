class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = dict()
        for i, num in enumerate(nums):
            if num in lookup and i - lookup[num] <= k:
                return True
            lookup[num] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], k=3))
print(s.containsNearbyDuplicate([1, 0, 1, 1], k=1))
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], k=2))
