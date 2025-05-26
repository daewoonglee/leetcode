from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = Counter(stones)
        return sum([c[jewel] if jewel in c else 0 for jewel in set(jewels)])


s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb")) # 3
print(s.numJewelsInStones("z", "ZZ")) # 0
