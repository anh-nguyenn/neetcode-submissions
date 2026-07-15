class Solution:
    def scoreOfString(self, s: str) -> int:
        start = int(ord(s[0])- ord('a'))
        if not s: return 0
        if len(s) == 1: return start
        res = 0
        for i in range(1, len(s)):
            res += abs(int(ord(s[i]) - ord(s[i-1])))
        return res