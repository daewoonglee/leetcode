class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        vowel = ["a", "e", "i", "o", "u"]
        for i, s in enumerate(sentence.split()):
            if s[0].lower() in vowel:
                new_s = s + "ma"
            else:
                new_s = s[1:] + s[0] + "ma"
            ans.append(new_s + "a" * (i+1))
        return " ".join(ans)


s = Solution()
# print(s.toGoatLatin("I speak Goat Latin")) # Imaa peaksmaaa oatGmaaaa atinLmaaaaa
# print(s.toGoatLatin("The quick brown fox jumped over the lazy dog")) # heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa
print(s.toGoatLatin("U u"))