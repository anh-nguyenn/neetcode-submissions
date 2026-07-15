class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} #signature -> groups
        for word in strs:
            sign = self.getSignature(word)
            if sign not in groups:
                groups[sign] = []
            groups[sign].append(word)
        return list(groups.values())
    def getSignature(self, word: str) -> str:
        M = {}
        for ch in word:
            M[ch] = 1+ M.get(ch, 0) 
        return ''.join(f"{k}{v}" for k, v in sorted(M.items()))
