class Solution:
    def isPalindrome(self, s: str) -> bool:
        def clean(s):
            res = ""
            for i in s:
                if i.isalnum():
                    res += i.lower()
            return res
        clean_s = clean(s)
        i, j = 0, len(clean_s) - 1
        while i < j:
            if clean_s[i] != clean_s[j]:
                return False
            i += 1
            j -= 1
        return True

    