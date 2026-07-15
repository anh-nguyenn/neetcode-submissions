class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if abs(n - m) > 1:
            return False
        if n == m:
            cnt = 0
            for i in range(n):
                if s[i] != t[i]:
                    cnt += 1
            return cnt == 1
        
        smaller = s if n < m else t
        bigger = t if n < m else s
        for i in range(len(smaller)):
            if smaller[i] != bigger[i]:
                return smaller[i:] == bigger[i+1:]
        return True