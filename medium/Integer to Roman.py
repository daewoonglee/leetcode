class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_dict = {
            1000: {1000: "M"},
            100: {500: "D", 100: "C"},
            10: {50: "L", 10: "X"},
            1: {5: "V", 1: "I"}
        }
        subtract_form = {4: "IV", 40: "XL", 400: "CD", 9: "IX", 90: "XC", 900: "CM"}
        ans = ""

        for i in [1000, 100, 10, 1]:
            q = num // i
            target = q*i
            num -= target

            if str(target)[0] in ["4", "9"]:
                ans += subtract_form[target]
            else:
                for k, v in symbol_dict[i].items():
                    if target >= k:
                        q = target // k
                        target -= k*q
                        ans += v*q
            print(f"target: {target}, ans: {ans}")
        return ans


s = Solution()
# print(s.intToRoman(3749)) # MMMDCCXLIX
# print(s.intToRoman(58)) # LVIII
# print(s.intToRoman(1994)) # MCMXCIV
# print(s.intToRoman(400)) # CD
print(s.intToRoman(49)) # XLIX
