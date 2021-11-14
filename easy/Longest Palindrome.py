class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = dict()
        for ch in s:
            if ch not in data:
                data[ch]=0
            data[ch]+=1
        ans = 0
        is_one = False
        for v in data.values():
            # 0.06960721500217915
            #if v%2==0: ans += v
            #else: ans += v-1; is_one = True

            # code refactoring (R) - 0.06984644429758191
            ans += (v // 2 * 2)
            if not is_one and v % 2 == 1: is_one = True
        return ans+1 if is_one else ans




s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("abcde"))
print(s.longestPalindrome("aaabbbccccdd"))
print(s.longestPalindrome("aaabccccdd"))


if __name__ == '__main__':
    from timeit import Timer
    query = ["abccccdd", "a", "abcde", "aaabbbccccdd", "aaabccccdd"]
    t = Timer(f"for t in {query}: Solution().longestPalindrome(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

