class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            arr = [0]*26
            for c in word:
                order = ord(c) - 97
                arr[order] += 1
            k = tuple(arr)
            hmap[k].append(word)
        return list(hmap.values())