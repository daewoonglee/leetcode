class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        N = len(bits)
        if N == 1:
            return not bool(bits[0])

        i = 0
        while i < N-1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == N-1


s = Solution()
# print(s.isOneBitCharacter([1,0,0])) # true
# print(s.isOneBitCharacter([1,1,1,0])) # false
# print(s.isOneBitCharacter([0,0])) # true
print(s.isOneBitCharacter([1])) # false
print(s.isOneBitCharacter([0,1,0])) # false
