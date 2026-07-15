class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        seen = set()
        for w in words:
            for i in words:  
                if i != w and w in i and w not in seen:
                    res.append(w)
                    seen.add(w)
        return res