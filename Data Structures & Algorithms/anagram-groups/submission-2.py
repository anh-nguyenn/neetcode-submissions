class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            arr = [0]*26
            for c in w:
                idx = ord(c) - ord('a')
                arr[idx] += 1
            # k = ''.join(list(map(str, arr)))
            k = tuple(arr)
            res[k].append(w)
        return list(res.values())