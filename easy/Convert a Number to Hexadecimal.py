class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 0.24172726273536682
        #hex_li = "0123456789abcdef"
        #hex_num=[]
        #if num < 0:
        #    #num = (2**32-1)+num+1

        #    # code refactoring (R) 01 - 0.24057982303202152
        #    num &= (2**32-1)
        #elif num == 0:
        #    return "0"
        #while num > 0:
        #    #num, d = divmod(num, 16)
        #    #hex_num.append(hex_li[d])

        #    # code refactoring (R) 02 - 0.19624112080782652 (call function이 없어서)
        #    hex_num.append(hex_li[num % 16])
        #    num //= 16
        #return ''.join(hex_num[::-1])

        # code refactoring (R) 03 - 0.21813468914479017
        hex_li = "0123456789abcdef"
        hex_num = []
        if num < 0:
            num &= (2**32-1)
        elif num == 0:
            return "0"
        while num > 0:
            hex_num.append(hex_li[num & 15])
            num >>= 4
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
print(s.toHex(2**31-1))
print(s.toHex(0))
print(s.toHex(-1))
print(s.toHex(-2))
print(s.toHex(-3))
print(s.toHex(-15))
print(s.toHex(-16))
print(s.toHex(-17))


if __name__ == '__main__':
    from timeit import Timer
    query = [26, 15, 16, 17, 32, 33, 160, 255, 256, 2**12-1, 2**31-1, 0, -1, -2, -3, -15, -16, -17, -2**30]
    t = Timer(f"for t in {query}: Solution().toHex(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

