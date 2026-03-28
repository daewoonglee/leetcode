class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # remove left whitespace

        if not s:
            return 0

        MAX = pow(2, 31)-1
        MIN = -pow(2, 31)

        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in ['-', '+'] else s

        res = []
        for ch in s:
            if ch.isdigit():
                res.append(ch)
            else:
                break

        if not res:
            return 0

        ans = int("".join(res)) * sign
        return max(MIN, min(MAX, ans))


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
