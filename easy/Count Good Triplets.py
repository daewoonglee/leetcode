class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        ans = 0
        for i in range(N-2):
            for j in range(i+1, N-1):
                if abs(arr[i] - arr[j]) > a: continue
                for k in range(j+1, N):
                    if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        ans += 1
        return ans


s = Solution()
# print(s.countGoodTriplets([3,0,1,1,9,7], a=7, b=2, c=3)) # 4
# print(s.countGoodTriplets([1,1,2,2,3], a=0, b=0, c=1)) # 0
print(s.countGoodTriplets([0,0,0,0,0], a=0, b=0, c=0)) # 0
