class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        ans = ""
        for value, symbol in symbols:
            while num >= value:
                ans += symbol
                num -= value
        return ans


s = Solution()
# print(s.intToRoman(3749)) # MMMDCCXLIX
# print(s.intToRoman(58)) # LVIII
# print(s.intToRoman(1994)) # MCMXCIV
# print(s.intToRoman(400)) # CD
print(s.intToRoman(49)) # XLIX
