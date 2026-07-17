import array as array
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for ch in strs:
            arr = [0]*26
            for c in ch:
                idx = ord(c) - ord('a')
                arr[idx] += 1
            hmap[tuple(arr)].append(ch)
        return list(hmap.values())
