from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {} # signature -> word
        for word in strs:
            sign = ''.join(sorted(word))
            if sign not in hmap:
                hmap[sign] = []
            hmap[sign].append(word)
        return list(hmap.values())