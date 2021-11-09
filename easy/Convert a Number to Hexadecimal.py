class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_li = "0123456789abcdef"
        print(f"num: {num}, d: {num//16}, mul: {16 * (num//16)}, hex: {hex(num)}")
        hex_num=[]
        #while num > 15:
        #    q, num = divmod(num, 16)
        #    print(f"q: {q}")
        #    hex_num.append(hex_li[q])
        #hex_num.append(hex_li[num])
        while num > 0:
            num, d = divmod(num, 16)
            hex_num.append(hex_li[d])
        return ''.join(hex_num[::-1])

s = Solution()
print(s.toHex(26))
print(s.toHex(15))
print(s.toHex(16))
print(s.toHex(17))
print(s.toHex(32))
print(s.toHex(33))
print(s.toHex(160))
print(s.toHex(2**31-1))
print(s.toHex(-1))

