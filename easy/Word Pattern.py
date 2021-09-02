class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
#        s_split_list = s.split()
#        if len(pattern) != len(s_split_list):
#            return False
#        log = dict()
#        for p, s_word in zip(pattern, s_split_list):
#            if p not in log:
#                if s_word in log.values():
#                    return False
#                log[p] = s_word
#            elif log[p] != s_word:
#                return False
#        return True

        # code refactoring (R) 01 - 
        # s_split_list = s.split()
        # return len(set(zip(s_split_list, pattern))) == len(set(s_split_list)) == len(set(pattern)) and len(s_split_list) == len(pattern)

        # code refactoring (R) 02 - 0.20034792
        s_split_list = s.split()
        if len(pattern) != len(s_split_list):
            return False
        log = dict()
        for p, s_word in zip(pattern, s_split_list):
            if p not in log:
                log[p] = s_word
            elif log[p] != s_word:
                return False
        return len(log) == len(set(s_split_list))


s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("aba", "dog dog dog cat"))      # F
print(s.wordPattern("aaa", "a a a a"))              # F
print(s.wordPattern("aaaaaaaaaaaaaa", "dog dog dog dog dog dog dog dog dog dog dog dog dog dog"))   # T
print(s.wordPattern("aaaaaaaaaaaaab", "dog dog dog dog dog dog dog dog dog dog dog dog dog dog"))   # F
print(s.wordPattern("abcdefghijklmnopqrstuvwxyz", "a b c d e f g h i j k l m n o p q r s t u v w x y z"))   # T


if __name__ == '__main__':
    from timeit import Timer
    query = [["abba", "dog cat cat dog"],
             ["abba", "dog cat cat fish"],
             ["abba", "dog dog dog dog"],
             ["aba", "dog dog dog cat"],
             ["aaa", "a a a a"],
             ["aaaaaaaaaaaaaa", "dog dog dog dog dog dog dog dog dog dog dog dog dog dog"],
             ["aaaaaaaaaaaaab", "dog dog dog dog dog dog dog dog dog dog dog dog dog dog"],
             ["abcdefghijklmnopqrstuvwxyz", "a b c d e f g h i j k l m n o p q r s t u v w x y z"]]
    t = Timer(f"for t in {query}: Solution().wordPattern(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

