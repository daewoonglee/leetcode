class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def comb(i):
            if i >= N:
                return phone_letter[digits[i]]

            row = comb(i+1)
            letter_comb = [f"{ch}{r}" for ch in phone_letter[digits[i]] for r in row]
            return letter_comb

        phone_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        N = len(digits)-1
        return comb(0)


s = Solution()
print(s.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(s.letterCombinations("2")) # ["a","b","c"]
print(s.letterCombinations("76"))
print(s.letterCombinations("999"))
