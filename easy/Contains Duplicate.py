import heapq
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 0.533448479
        # nums.sort()
        # for i, n in enumerate(nums[:-1]):
        #     if n == nums[i+1]:
        #         return True
        # return False

        # 23.203082602000002
        # lookup = bytearray(150000)
        lookup = bytearray(10000)
        for n in nums:
            idx = n >> 3
            is_exist = 1 << (n & 7)
            if lookup[idx] & is_exist:
                return True
            lookup[idx] |= is_exist
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
# print(s.containsDuplicate([1, 2, 3, 4]))
# print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# print(s.containsDuplicate([1, 2, 3, 3, 4]))
# print(s.containsDuplicate([1, 1]))
# print(s.containsDuplicate([1, 1, 1, 1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1, 2, 3, 1],
             [1, 2, 3, 4],
             [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
             list(range(10000)) + [9999]]
    t = Timer(f"for t in {query}: Solution().containsDuplicate(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
