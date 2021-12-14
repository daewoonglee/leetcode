class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pts = -1
        max_n = 0
        for i, n in enumerate(nums):
            if not n and pts != -1:
                if i-pts > max_n:
                    max_n = i-pts
                pts = -1
            elif n and pts == -1:
                pts = i
        if pts != -1 and len(nums)-pts > max_n:
            max_n = len(nums)-pts
        return max_n


s = Solution()
print(s.findMaxConsecutiveOnes([0,0,0,1,1,0,0,1,1,1]))
print(s.findMaxConsecutiveOnes([1,1,1,0,0,1,1,0,0,0]))

