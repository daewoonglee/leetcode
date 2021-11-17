class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ascii_code = {i: ord(i) for i in "0123456789"}
        min_n, max_n, min_num, max_num = (len(num1), len(num2), num1, num2) if len(num1) < len(num2) else (len(num2), len(num1), num2, num1)
        i = -1
        ans = []
        q = "0"
        while abs(i) <= min_n:
            calc_num = str((ascii_code[min_num[i]] + ascii_code[max_num[i]] + ascii_code[q]) - 144)
            q = calc_num[0] if len(calc_num) >= 2 else "0"
            d = calc_num[-1]
            i -= 1
            # print(f"sum: {calc_num}, q: {q}, d: {d}")
            ans.append(d)
        while abs(i) <= max_n:
            calc_num = str((ascii_code[max_num[i]] + ascii_code[q]) - 96)
            q = calc_num[0] if len(calc_num) >= 2 else "0"
            d = calc_num[-1]
            i -= 1
            # print(f"max sum: {calc_num}, q: {q}, d: {d}")
            ans.append(d)
        return "".join(ans[::-1] if q == "0" else [q] + ans[::-1])


s = Solution()
print(s.addStrings("1", "2"))
print(s.addStrings("1", "8"))
print(s.addStrings("1", "9"))
print(s.addStrings("1", "100"))

