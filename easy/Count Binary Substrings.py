class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def search_group(i):
            if i >= N:
                return i

            target = s[i]
            for j in range(i+1,  N, 1):
                if target == s[j]:
                    i += 1
                else:
                    break
            return i

        N = len(s)
        cur_idx, tail_idx = 0, N
        ans = 0
        while 1:
            cur_idx = search_group(cur_idx)
            tail_idx = search_group(cur_idx+1)
            print(f"cur: {cur_idx}, tail: {tail_idx}")
            if tail_idx == N: break
            ans += tail_idx - cur_idx
            cur_idx += 1
        return ans


s = Solution()
# print(s.countBinarySubstrings("00110011"))  # 6
# print(s.countBinarySubstrings("000111"))    # 3
# print(s.countBinarySubstrings("10101"))     # 4
# print(s.countBinarySubstrings("1"))         # 0
# print(s.countBinarySubstrings("111"))       # 0
print(s.countBinarySubstrings("00100"))     # 2
