class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # 0.07147948071360588
        #if len(timeSeries) == 1:
        #    return duration
        #
        #ans = 0
        #for i, ts in enumerate(timeSeries[:-1]):
        #    if ts + duration - 1 < timeSeries[i+1]:
        #        ans += duration
        #    else:
        #        ans += timeSeries[i+1] - ts
        #if timeSeries[-2] <= timeSeries[-1]:
        #    ans += duration
        #return ans

        # code refactoring - 0.06547707878053188
        #ans = 0
        #for i, ts in enumerate(timeSeries[:-1]):
        #    ans += duration if ts + duration -1 < timeSeries[i+1] else timeSeries[i+1]-ts
        #return ans + duration

        # code refactoring (R) - 0.057625443674623966
        ans = 0
        for i, ts in enumerate(timeSeries[:-1]):
            diff = timeSeries[i+1] - ts
            ans += diff if diff < duration else duration
        return ans + duration




s = Solution()
print(s.findPoisonedDuration([1, 4], 2))
print(s.findPoisonedDuration([1, 4, 7], 3))
print(s.findPoisonedDuration([1, 2], 2))
print(s.findPoisonedDuration([1, 2, 3], 2))
print(s.findPoisonedDuration([0], 3))

if __name__ == '__main__':
    from timeit import Timer
    query = [[[1, 4], 2], [[1, 4, 7], 3], [[1, 2], 2], [[1, 2, 3], 2], [[0], 3], [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], 2]]
    t = Timer(f"for t in {query}: Solution().findPoisonedDuration(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

