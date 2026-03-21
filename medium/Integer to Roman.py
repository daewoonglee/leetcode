class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_dict = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        rev_values = list(reversed(symbol_dict.keys()))
        ans = ""
        while num >= 4:
            if str(num)[0] in ["4", "9"]:
                for v in rev_values:
                    if num < v:
                        diff = v//10 # 4가 들어오면 0이 나오는 케이스 발생
                        diff_num = v-num//diff*diff
                        num -= (v-diff_num)
                        ans += symbol_dict[diff_num]
                        ans += symbol_dict[v]
                        break
            else:
                for value, symbol in symbol_dict.items():
                    if num > value:
                        num %= value
                        ans += symbol
                        break
        if num != 0:
            for _ in range(num):
                ans += symbol_dict[1]
        return ans


s = Solution()
# print(s.intToRoman(3749)) # MMMDCCXLIX
# print(s.intToRoman(58)) # LVIII
print(s.intToRoman(1994)) # MCMXCIV
# print(s.intToRoman(400)) # CD
