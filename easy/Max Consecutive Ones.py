class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.2462407052516937
        #pts = -1
        #max_n = 0
        #for i, n in enumerate(nums):
        #    if not n and pts != -1:
        #        if i-pts > max_n:
        #            max_n = i-pts
        #        pts = -1
        #    elif n and pts == -1:
        #        pts = i
        #if pts != -1 and len(nums)-pts > max_n:
        #    max_n = len(nums)-pts
        #return max_n

        # code refactoring (R) - 1.0491484282538295
        #max_n = 0
        #cnt = 0
        #for n in nums:
        #    if n:
        #        cnt += 1
        #    else:
        #        cnt = 0
        #    if cnt > max_n:
        #        max_n = cnt
        #return max_n

        # code refactoring (R) 02 - 0.7625838806852698
        max_n = 0
        cnt = 0
        for n in nums:
            if n:
                cnt += 1
            else:
                if cnt and cnt > max_n:
                    max_n = cnt
                cnt = 0
        return max_n if cnt < max_n else cnt 


s = Solution()
print(s.findMaxConsecutiveOnes([0,0,0,1,1,0,0,1,1,1]))
print(s.findMaxConsecutiveOnes([1,1,1,0,0,1,1,0,0,0]))
print(s.findMaxConsecutiveOnes([1]*1000))


if __name__ == '__main__':
    from timeit import Timer
    query = [[0,0,0,1,1,0,0,1,1,1], [1,1,1,0,0,1,1,0,0,0], [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0], [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1], [1]*1000, [0]*1000]
    t = Timer(f"for t in {query}: Solution().findMaxConsecutiveOnes(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

