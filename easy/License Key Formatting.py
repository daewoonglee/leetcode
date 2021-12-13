class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 0.31685654167085886
        #rep_s = s.replace("-", "")
        #idx = len(rep_s) % k
        #ans = [rep_s[:idx].upper()] if idx else []
        #temp = []
        #for ch in rep_s[idx:]:
        #    temp.append(ch)
        #    if len(temp) == k:
        #        ans.append("".join(temp).upper())
        #        temp.clear()
        #return "-".join(ans)

        # code refactoring 01 - 0.27237985096871853
        #rep_s = s.replace("-", "")
        #N = len(rep_s)
        #idx = N % k
        #ans = [rep_s[:idx].upper()] if idx else []
        #while idx < N:
        #    ans.append("".join(rep_s[idx: idx+k].upper()))
        #    idx += k
        #return "-".join(ans)

        # code refactoring 02 - 0.15801248606294394
        #rep_s = s.replace("-", "")
        #N = len(rep_s)
        #idx = N % k
        #ans = "-".join(([rep_s[:idx].upper()] if idx else []) + [rep_s[i: i+k].upper() for i in range(idx, N, k)])
        #return ans

        # code refactoring (R) - 0.129369187168777 (method callback 차이)
        #rep_s = s.replace("-", "").upper()
        #N = len(rep_s)
        #idx = N % k
        #ans = "-".join(([rep_s[:idx]] if idx else []) + [rep_s[i: i+k] for i in range(idx, N, k)])
        #return ans


s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-2", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
print(s.licenseKeyFormatting("2-5g-3-J1", 2))
print(s.licenseKeyFormatting("222222222222", 1))
print(s.licenseKeyFormatting("2-4A0r7-4k", 4))


if __name__ == '__main__':
    from timeit import Timer
    query = [["5F3Z-2e-9-2", 4], ["2-5g-3-J", 2], ["2-5g-3-J1", 2], ["222222222222", 1], ["2-4A0r7-4k", 4], ["a"*100, 3]]
    t = Timer(f"for t in {query}: Solution().licenseKeyFormatting(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

