class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        # N = len(nums)
        # nums.sort()
        # ans = ""
        # for i in range(2**N):
        #     ans = bin(i)[2:].zfill(N)
        #     if ans not in nums:
        #         break
        # return ans

        # code refactoring 02
        # N = len(nums)
        # binary_li = [0 for _ in range(2**N)]
        # for n in nums:
        #     binary_li[int(n, 2)] = 1
        # for i, b in enumerate(binary_li):
        #     if b == 0:
        #         return bin(i)[2:].zfill(N)
        # return ""

        # code refactoring 03 - 문제에선 nums 배열의 길이는 최대 n을 넘지 않음 (이 부분을 제대로 이해 못하고 풀었음)
        return "".join(['1' if n[i] == '0' else '0' for i, n in enumerate(nums)])


s = Solution()
# print(s.findDifferentBinaryString(["01", "10"])) # 11 or 00
# print(s.findDifferentBinaryString(["00", "01"])) # 11 or 10
print(s.findDifferentBinaryString(["111", "011", "001"])) # 101 or 000 or 010 or 100 or 110
