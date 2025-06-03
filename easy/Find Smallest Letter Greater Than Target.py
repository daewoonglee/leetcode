class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        letters.sort()
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]


s = Solution()
print(s.nextGreatestLetter(["c","f","j"], "a")) # c
print(s.nextGreatestLetter(["c","f","j"], "c")) # f
print(s.nextGreatestLetter(["x","x","y","y"], "z")) # x
