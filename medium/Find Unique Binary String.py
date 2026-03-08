class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        N = len(nums)
        ans = set(bin(i)[2:].zfill(N) for i in range(2**N))
        for n in nums:
            if n in ans:
                ans.remove(n)
        return ans.pop()


s = Solution()
# print(s.findDifferentBinaryString(["01", "10"])) # 11 or 00
# print(s.findDifferentBinaryString(["00", "01"])) # 11 or 10
print(s.findDifferentBinaryString(["111", "011", "001"])) # 101 or 000 or 010 or 100 or 110
