class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 1:
            return duration

        ans = 0
        for i, ts in enumerate(timeSeries[:-1]):
            if ts + duration - 1 < timeSeries[i+1]:
                ans += duration
            else:
                ans += timeSeries[i+1] - ts
        if timeSeries[-2] <= timeSeries[-1]:
            ans += duration
        return ans


s = Solution()
print(s.findPoisonedDuration([1, 4], 2))
print(s.findPoisonedDuration([1, 2], 2))
print(s.findPoisonedDuration([0], 3))
