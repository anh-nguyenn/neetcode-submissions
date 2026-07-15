class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hmap = defaultdict(int)
        for w in arr:
            hmap[w] += 1
        res = []
        for ky, v in hmap.items():
            if v != 1:
                continue
            res.append(ky)
        k = k - 1
        if k > len(res) - 1:
            return ""
        return res[k]
            