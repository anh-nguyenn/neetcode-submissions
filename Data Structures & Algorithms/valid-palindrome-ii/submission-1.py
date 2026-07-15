class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPaldndrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l+1:r+1]
                skipR = s[l:r]
                return isPaldndrome(skipL) or isPaldndrome(skipR)
            l, r = l + 1, r - 1
        return True
        