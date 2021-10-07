class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 0.05270291503984481
        # return list(set(nums1).intersection(set(nums2)))

        # code refactoring (R) 01 - 0.05021924898028374
        # return list(set(nums1) & set(nums2))

        # code refactoring (R) 02 - 0.05505535809788853
        ans = []
        log = dict()
        for n in nums1:
            if n not in log:
                log[n] = 1
        for n in nums2:
            if n in log and log[n]:
                ans.append(n)
                log[n] = 0
        return ans


s = Solution()
print(s.intersection([2,2], nums2=[2,2]))
print(s.intersection([1,2,2,1], nums2=[2,2]))
print(s.intersection([4,9,5], nums2=[9,4,9,8,4]))
print(s.intersection([1,1,1,1,1,1,1,1,1,1,1,1,1], nums2=[9,4,9,8,4,1]))
print(s.intersection([1,1,1,1,1,1,1,1,1,1,1,1,2,1], nums2=[9,4,9,8,4,1,2]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[2,2], [2,2]], [[1,2,2,1], [2,2]], [[4,9,5], [9,4,9,8,4]], [[1,1,1,1,1,1,1,1,1,1,1,1,1], [9,4,9,8,4,1]], [[1,1,1,1,1,1,1,1,1,1,1,1,2,1], [9,4,9,8,4,1,2]]]
    t = Timer(f"for t in {query}: Solution().intersection(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

