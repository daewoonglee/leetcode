class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 0.05672426900000001
        # s = list(s)
        # vowels = ["a", "e", "i", "o", "u"]
        # idxs = []
        # for i, w in enumerate(s):
        #     if w.lower() in vowels:
        #         idxs.append(i)

        # for i in range(len(idxs) // 2):
        #     t = s[idxs[i]]
        #     s[idxs[i]] = s[idxs[-1 - i]]
        #     s[idxs[-1 - i]] = t

        # return "".join(s)
       
        # code refactoring 01 - 0.044005323
        # s = list(s)
        # vowels = "aeiou"
        # i, j = 0, len(s) - 1
        # while i < j:
        #     while i < j and s[i].lower() not in vowels:
        #         i += 1
        #     while i < j and s[j].lower() not in vowels:
        #         j -= 1
        #
        #     t = s[i]
        #     s[i] = s[j]
        #     s[j] = t
        #
        #     i += 1
        #     j -= 1
        # return "".join(s)

        # code refactoring 02 - 0.04350535899999999
        s = list(s)
        vowels = "aeiou"
        i, j = 0, len(s)-1
        while i < j:
            if s[i].lower() not in vowels:
                i += 1
                continue
            if s[j].lower() not in vowels:
                j -= 1
                continue
            if i < j:
                t = s[i]
                s[i] = s[j]
                s[j] = t

                i+=1
                j-=1
        return "".join(s)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("hellO"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["Hello", "test", "testtesttest"]
    t = Timer(f"for t in {query}: Solution().reverseVowels(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
 
