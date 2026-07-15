class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        n = len(s)
        if not s:
            return 
        i = n - 1
        while i >= 0:
            print(s[i])
            if not s[i].isalpha():
                i -= 1
                continue
            print(s[i])
            while i >= 0 and s[i] != " ":
                res += 1
                i -= 1
            break
        return res
        