class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrAna = [0]*26
        print(arrAna)
        for i in range(len(s)):
            arrAna[ord(s[i]) - ord('a')] += 1
            arrAna[ord(t[i]) - ord('a')] -= 1
        for n in arrAna:
            if n != 0:
                return False
        return True