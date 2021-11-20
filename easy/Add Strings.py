class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 0.2059301771223545
        #ascii_code = {i: ord(i)-ord("0") for i in "0123456789"}
        #min_n, max_n, min_num, max_num = (len(num1), len(num2), num1, num2) if len(num1) < len(num2) else (len(num2), len(num1), num2, num1)
        #i = -1
        #ans = []
        #q = "0"
        #while abs(i) <= min_n:
        #    calc_num = str((ascii_code[min_num[i]] + ascii_code[max_num[i]] + ascii_code[q]))
        #    q = calc_num[0] if len(calc_num) >= 2 else "0"
        #    d = calc_num[-1]
        #    i -= 1
        #    ans.append(d)
        #while abs(i) <= max_n:
        #    calc_num = str((ascii_code[max_num[i]] + ascii_code[q]))
        #    q = calc_num[0] if len(calc_num) >= 2 else "0"
        #    d = calc_num[-1]
        #    i -= 1
        #    ans.append(d)
        #return "".join(ans[::-1] if q == "0" else [q] + ans[::-1])

        # code refactoring (R) - 0.1175075164064765
        ascii_code = {i: ord(i)-ord("0") for i in "0123456789"}
        n1 = n2 = 0
        for i in num1:
            n1 = n1*10 + ascii_code[i]
        for i in num2:
            n2 = n2*10 + ascii_code[i]
        return str(n1 + n2)


s = Solution()
print(s.addStrings("1", "2"))
print(s.addStrings("1", "8"))
print(s.addStrings("1", "9"))
print(s.addStrings("1", "100"))


if __name__ == '__main__':
    from timeit import Timer
    query = [["1", "10000"], ["1234", "3214"], ["1111", "11111"], ["12345", "54321"], ["9999", "1"]]
    t = Timer(f"for t in {query}: Solution().addStrings(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

