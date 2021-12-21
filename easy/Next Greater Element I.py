class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 0.1555284485220909
        #ans = []
        #for n1 in nums1:
        #    # find index
        #    #idx = 0
        #    #for i, n2 in enumerate(nums2):
        #    #    if n1 == n2:
        #    #        idx = i
        #    #        break
        #    idx = nums2.index(n1)
        #    n = nums2[idx]
        #    flag = False
        #    for i, n2 in enumerate(nums2[idx+1:]):
        #        if n < n2:
        #            ans.append(n2)
        #            flag=True
        #            break
        #    if not flag:
        #        ans.append(-1)
        #return ans

        # code refactoring (R) - 0.09087799768894911
        stack = []
        dic = {}
        for n2 in nums2:
            while stack and n2 > stack[-1]:
                dic[stack.pop()] = n2
            stack.append(n2)
        ans = [dic[n1] if n1 in dic else -1 for n1 in nums1]
        return ans


s = Solution()
#print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
#print(s.nextGreaterElement([4,1,2], [1,2,0,4]))
print(s.nextGreaterElement([3,2,1], [1,2,3,4]))
print(s.nextGreaterElement([1,2,3], [4,3,2,1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[4,1,2], [1,3,4,2]], [[4,1,2], [1,2,0,4]], [[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9,10]], [[9,8,7,6,5,4,3,2,1], [10,9,8,7,6,5,4,3,2,1]]]
    t = Timer(f"for t in {query}: Solution().nextGreaterElement(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

