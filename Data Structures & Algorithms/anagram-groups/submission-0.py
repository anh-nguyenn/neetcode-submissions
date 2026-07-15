class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # format: a1c1t1; 
        # format: {signature -> list of words for this signature}
        groups = {}
        for ch in strs:
            signature = self.getSignature(ch)
            if signature not in groups:
                groups[signature] = []
            groups[signature].append(ch)
        return list(groups.values())

    def getSignature(self, word: str) -> str:
        freq = {}
        for c in word:
            freq[c] = 1 + freq.get(c, 0)
        freq_sorted = sorted(freq.items())
        return ''.join(f"{k}{v}" for k, v in freq_sorted)
    
        