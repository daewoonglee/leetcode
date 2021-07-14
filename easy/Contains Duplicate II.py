class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 1.9851560299999997
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
print(s.containsNearbyDuplicate(list(range(1000)) + [0], k=1000))
print(s.containsNearbyDuplicate(list(range(1000)) + [0], k=999))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[1, 2, 3, 1], 3],
             [[1, 0, 1, 1], 1],
             [[1, 2, 3, 1, 2, 3], 2],
             [list(range(1000)) + [0], 1000],
             [list(range(1000)) + [0], 999]]
    t = Timer(f"for t in {query}: Solution().containsNearbyDuplicate(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
