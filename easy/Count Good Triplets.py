from bisect import bisect_left


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        ans = 0
        for j in range(1, N-1):
            left = [arr[i] for i in range(j) if abs(arr[i] - arr[j]) <= a]
            right = [arr[k] for k in range(j+1, N) if abs(arr[j] - arr[k]) <= b]
            right.sort()

            for l in left:
                ans += bisect_left(right, l+c+1) - bisect_left(right, l-c)
        return ans


s = Solution()
# print(s.countGoodTriplets([3,0,1,1,9,7], a=7, b=2, c=3)) # 4
# print(s.countGoodTriplets([1,1,2,2,3], a=0, b=0, c=1)) # 0
print(s.countGoodTriplets([0,0,0,0,0], a=0, b=0, c=0)) # 10
