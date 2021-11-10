class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_li = "0123456789abcdef"
        # print(f"num: {num}, d: {num//16}, mul: {16 * (num//16)}, hex: {hex(num)}")
        hex_num=[]
        if num < 0:
            num = (2**32-1)+num+1
        elif num == 0:
            return "0"
        while num > 0:
            num, d = divmod(num, 16)
            hex_num.append(hex_li[d])
        return ''.join(hex_num[::-1])


s = Solution()
#print(s.toHex(26))
#print(s.toHex(15))
#print(s.toHex(16))
#print(s.toHex(17))
#print(s.toHex(32))
#print(s.toHex(33))
#print(s.toHex(160))
#print(s.toHex(255))
#print(s.toHex(256))
#print(s.toHex(2**12-1))
#print(s.toHex(2**31-1))
print(s.toHex(0))
print(s.toHex(-1))
print(s.toHex(-2))
print(s.toHex(-3))
print(s.toHex(-15))
print(s.toHex(-16))
print(s.toHex(-17))

