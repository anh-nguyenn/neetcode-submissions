class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        window = set()
        L, R = 0, 0
        length = 1
        for R in range(len(s)):
            # if s[R] in window:
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            length = max(length,len(window))
        return length
        