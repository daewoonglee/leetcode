class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        for i in range(len(s)):
            if s[i:]+s[:i] == goal: return True
        return False


s = Solution()
print(s.rotateString("abcde", "cdeab")) # True
print(s.rotateString("abcde", "abced")) # False
print(s.rotateString("abcabced", "abcedabc")) # True
print(s.rotateString("defdefdefabcabc", "defdefabcabcdef")) # True
