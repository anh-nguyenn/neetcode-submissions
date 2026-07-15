class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            return (ord('a') <= ord(c) <= ord('z') or 
                    ord('A') <= ord(c) <= ord('Z') or 
                    ord('0') <= ord(c) <= ord('9'))
        # instead of user isalnum()

        l, r = 0, len(s) - 1
        while l < r:
            if not isAlphaNum(s[l]):
                l += 1
                continue
            if not isAlphaNum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                print(s[l].lower())
                print(s[r].lower())
                return False
            l, r = l + 1, r - 1
        return True