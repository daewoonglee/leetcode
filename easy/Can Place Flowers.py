class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        N = len(flowerbed)
        if N <= 1:
            if n == 0: return True
            return True if not flowerbed[0] else False
        i = 0
        cnt = 0
        if not flowerbed[i] and not flowerbed[i+1]:
            flowerbed[i] = 1
            cnt += 1
            i += 1
        while i < N-1:
            if not flowerbed[i-1] and not flowerbed[i] and not flowerbed[i+1]:
                # print(f"i: {i}, cnt: {cnt}")
                cnt += 1
                flowerbed[i] = 1
            i += 1
        if i < N and not flowerbed[-1] and not flowerbed[-2]:
            cnt += 1
        return True if cnt >= n else False


s = Solution()
# print(s.canPlaceFlowers([1,0,0,0,1], 1)) # True
# print(s.canPlaceFlowers([1,0,0,0,1], 2)) # False
print(s.canPlaceFlowers([1], 1)) # False
print(s.canPlaceFlowers([1], 0)) # True
print(s.canPlaceFlowers([0], 0)) # True
print(s.canPlaceFlowers([0], 1)) # True
# print(s.canPlaceFlowers([1,0,0,0,0,0,1], 2)) # True
# print(s.canPlaceFlowers([1,0,0,0,0,1], 2)) # False
# print(s.canPlaceFlowers([1,0,0], 1)) # True
# print(s.canPlaceFlowers([0,1,0], 1)) # False
# print(s.canPlaceFlowers([0,0], 2)) # False
print(s.canPlaceFlowers([1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1], 2)) # False