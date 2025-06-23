class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for num in range(left, right+1):
            for ch in str(num):
                ch = int(ch)
                if ch <= 0 or num % ch != 0:
                    break
            else:
                ans.append(num)
        return ans


s = Solution()
print(s.selfDividingNumbers(1, 22)) # [1,2,3,4,5,6,7,8,9,11,12,15,22]
print(s.selfDividingNumbers(47, 85)) # [48,55,66,77]
