M = {
    ")":"(",
    "}":"{",
    "]":"["
}
class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        if s[0] in M:
            return False
        for c in s:
            if c in M.values():
                res.append(c)
            elif res and res[-1] == M[c]:
                res.pop()
            else:
                return False
        return len(res) == 0
                
        