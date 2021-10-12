class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i = j = 0
        ans = []

        # 0.12609540997073054
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] == nums2[j]:
        #         ans.append(nums1[i])
        #         i += 1
        #         j += 1
        #     elif nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums2[j] < nums1[i]:
        #         j += 1
        # return ans

        # code refactoring - 0.11539928603451699
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums2[j] < nums1[i]:
        #         j += 1
        #     else:
        #         ans.append(nums1[i])
        #         i += 1
        #         j += 1
        # return ans

        # code refactoring (R) - 0.08886186603922397
        cnt = dict()
        for n in nums1:
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n] += 1
        
        ans = []
        for n in nums2:
            if n in cnt and cnt[n]:
                ans.append(n)
                cnt[n] -= 1
        return ans

s = Solution()
print(s.intersect([1,2,2,1], [2,2]))
print(s.intersect([4,9,5], [9,4,9,8,4]))                
print(s.intersect([1,1,1,1,1,1,1,2], [1,2]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[2,2], [2,2]], [[1,2,2,1], [2,2]], [[4,9,5], [9,4,9,8,4]], [[1,1,1,1,1,1,1,1,1,1,1,1,1], [9,4,9,8,4,1]], [[1,1,1,1,1,1,1,1,1,1,1,1,2,1], [9,4,9,8,4,1,2]]]
    t = Timer(f"for t in {query}: Solution().intersect(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

