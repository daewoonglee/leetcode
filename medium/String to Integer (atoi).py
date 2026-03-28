class Solution:
    def myAtoi(self, s: str) -> int:
        def check_leading(leading_sign):
            idx = 0
            for i, ch in enumerate(s):
                if ch != leading_sign:
                    idx = i
                    break
            return idx

        idx = check_leading(" ")
        s = s[idx:]

        if not s:
            return 0

        UPPER = 2147483647
        DOWN = -2147483648

        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in ['-', '+'] else s

        idx = check_leading("0")
        s = s[idx:]

        res = []
        for ch in s:
            if 48 <= ord(ch) <= 57:
                res.append(ch)
            else:
                break

        ans = "".join(res)
        ans = int(ans) * sign if ans != '' else 0
        ans = UPPER if UPPER < ans else ans
        ans = DOWN if ans < DOWN else ans
        return ans


s = Solution()
# print(s.myAtoi("42")) # 42
# print(s.myAtoi("42 42")) # 42
# print(s.myAtoi("42-42")) # 42
# print(s.myAtoi(" -042")) # -42
# print(s.myAtoi("1337c0d3")) # 1337
# print(s.myAtoi("0-1")) # 0
# print(s.myAtoi("words and 987")) # 0
# print(s.myAtoi("2147483648")) # 2,147,483,647
# print(s.myAtoi("2147483647")) # 2,147,483,647
# print(s.myAtoi("")) # 0
# print(s.myAtoi("21474836460")) # 2147483647 # leading zero 이해X 했음
# print(s.myAtoi("  +0 123")) # 0 # leading whitespace 이해X 했음
print(s.myAtoi("+00131204")) # 131204 # leading whitespace 이해X 했음
