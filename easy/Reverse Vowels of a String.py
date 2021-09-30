class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ["a", "e", "i", "o", "u"]
        idxs = []
        for i, w in enumerate(s):
            if w.lower() in vowels:
                idxs.append(i)

        for i in range(len(idxs) // 2):
            t = s[idxs[i]]
            s[idxs[i]] = s[idxs[-1 - i]]
            s[idxs[-1 - i]] = t

        return "".join(s)
       

s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("hellO"))
 
