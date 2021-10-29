class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 0.39232960203662515
        #s = "".join(sorted(list(s)))
        #t = "".join(sorted(list(t)))
        #for w1, w2 in zip(s, t):
        #    if w1 != w2:
        #        return w2
        #return t[-1]

        # code refactoring - 0.6058247033506632
        #log = dict()
        #for w in t:
        #    if w not in log:
        #        log[w] = 0
        #    log[w] += 1
        #for w in s:
        #    if w not in log:
        #        return w
        #    log[w] -= 1
        #return [k for k,v in log.items() if v == 1][0]

        # code refactoring (R) 01 - 0.6349351177923381
        #log = dict()
        #for w in s:
        #    log[w] = log.get(w, 0) + 1
        #for w in t:
        #    if not log.get(w):
        #        return w
        #    log[w] -= 1

        # code refactoring (R) 02 - 0.3955998797900975
        #return chr(sum([ord(w2)-ord(w1) for w1, w2 in zip(s, t)]) + ord(t[-1]))

        # code refactoring (R) 03 - 0.22857620101422071
        add_letter = s + t
        for w in t:
            if add_letter.count(w) % 2 != 0:
                return w
 
s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("", "y"))
print(s.findTheDifference("a", "aa"))
print(s.findTheDifference("ae", "aea"))


if __name__ == '__main__':
    from timeit import Timer
    query = [["abcd", "abcde"], ["", "y"], ["a", "aa"], 
            ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"],
            ["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzz"], 
            ["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzz"],
            ["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzz"],
            ["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzd"]] 
    t = Timer(f"for t in {query}: Solution().findTheDifference(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

