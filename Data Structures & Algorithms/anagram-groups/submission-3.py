from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list) # signature -> word
        for word in strs:
            sign = ''.join(sorted(word))
            hmap[sign].append(word)
        res = []
        for val in hmap.values():
            res.append(val)
        return res