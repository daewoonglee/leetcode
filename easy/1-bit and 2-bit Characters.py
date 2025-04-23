class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        N = len(bits)
        i = 0
        ans = []
        while i < N:
            if bits[i] == 1:
                ans.append(bits[i:i+2])
                i += 2
            else:
                ans.append(bits[i])
                i += 1
        return True if ans[-1] == 0 else False


s = Solution()
# print(s.isOneBitCharacter([1,0,0])) # true
# print(s.isOneBitCharacter([1,1,1,0])) # false
# print(s.isOneBitCharacter([0,0])) # true
print(s.isOneBitCharacter([1])) # false
print(s.isOneBitCharacter([0,1,0])) # false
