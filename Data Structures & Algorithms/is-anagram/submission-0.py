class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False
        freqS = self.buildDict(s)
        freqT = self.buildDict(t)
        return freqS == freqT
        

    def buildDict(self,anagram):
        freq = {}
        for ch in anagram:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        return freq
