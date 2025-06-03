class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        letters.sort()
        if letters[-1] <= target: return letters[0]

        l, r = 0, len(letters)-1
        while l <= r:
            p = l + (r-l)//2
            if letters[p] <= target:
                l = p + 1
            else:
                r = p - 1
        return letters[l]


s = Solution()
print(s.nextGreatestLetter(["c","f","j"], "a")) # c
print(s.nextGreatestLetter(["c","f","j"], "c")) # f
print(s.nextGreatestLetter(["x","x","y","y"], "z")) # x
print(s.nextGreatestLetter(["x","y","z"], "z")) # x
