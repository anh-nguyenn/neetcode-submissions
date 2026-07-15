# Using hash table
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arrAnagram = [0]*26
        for i in range(len(s)):
            arrAnagram[ord(s[i]) - ord('a')] += 1 # key
            arrAnagram[ord(t[i]) - ord('a')] -= 1
        for val in  arrAnagram:
            if val != 0:
                return False
        return True  