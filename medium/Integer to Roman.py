class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_dict = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        rev_values = list(reversed(symbol_dict.keys()))
        ans = ""

        for i in [1000, 100, 10, 1]:
            q, d = divmod(num, i)
            target = q*i
            num -= target

            if str(target)[0] in ["4", "9"]:
                for rv in rev_values:
                    if target < rv:
                        ans += symbol_dict[rv-target]
                        ans += symbol_dict[rv]
                        break
            else:
                for k, v in symbol_dict.items():
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
