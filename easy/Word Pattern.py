class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_split_list = s.split()
        if len(pattern) != len(s_split_list):
            return False
        log = dict()
        for p, s_word in zip(pattern, s_split_list):
            if p not in log:
                if s_word in log.values():
                    return False
                log[p] = s_word
            elif log[p] != s_word:
                return False
        return True


s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("abba", "dog dog dog dog"))
 
