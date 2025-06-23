class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for num in range(left, right+1):
            temp = num
            while temp > 0:
                d = temp % 10
                if d == 0 or num % d != 0:
                    break
                temp //= 10
            else:
                ans.append(num)
        return ans


s = Solution()
print(s.selfDividingNumbers(1, 22)) # [1,2,3,4,5,6,7,8,9,11,12,15,22]
print(s.selfDividingNumbers(47, 85)) # [48,55,66,77]
