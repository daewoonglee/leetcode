class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        N = len(candyType)//2
        #unique_type = set(candyType)
        #return len(unique_type) if len(unique_type) <= N else N 

        cnt = 0
        candy_types = []
        for ct in candyType:
            if ct not in candy_types:
                cnt += 1
                candy_types.append(ct)
                if cnt >= N: return cnt
        return N if N < cnt else cnt


s = Solution()
print(s.distributeCandies([1,1,2,2,3,3]))
print(s.distributeCandies([1,1,1,1]))
print(s.distributeCandies([-1,0,1,2]))

