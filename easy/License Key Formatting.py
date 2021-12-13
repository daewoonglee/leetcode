class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        rep_s = s.replace("-", "")
        idx = len(rep_s) % k
        ans = [rep_s[:idx].upper()] if idx else []
        temp = []
        for ch in rep_s[idx:]:
            temp.append(ch)
            if len(temp) == k:
                ans.append("".join(temp).upper())
                temp.clear()
        return "-".join(ans)


s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-2", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
print(s.licenseKeyFormatting("2-5g-3-J1", 2))
print(s.licenseKeyFormatting("222222222222", 1))
print(s.licenseKeyFormatting("2-4A0r7-4k", 4))

