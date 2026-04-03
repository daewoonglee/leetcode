class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def comb(i):
            cur_idx = ord(digits[i]) - ord('2')
            if i == last_idx:
                return list(phone_letter[cur_idx])
            return [ch + r for ch in phone_letter[cur_idx] for r in comb(i+1)]

        phone_letter = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        last_idx = len(digits)-1
        return comb(0)


s = Solution()
print(s.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(s.letterCombinations("2")) # ["a","b","c"]
print(s.letterCombinations("76"))
print(s.letterCombinations("999"))
