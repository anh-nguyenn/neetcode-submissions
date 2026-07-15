class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.checkValid(s):
            return True
        # perform remove and check
        l, r = 0, len(s)
        for i in range(len(s)):
            dS = s[l:i] + s[i+1:r]
            if self.checkValid(dS):
                return True
        return False
    
    def checkValid(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        