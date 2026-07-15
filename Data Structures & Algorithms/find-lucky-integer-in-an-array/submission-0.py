class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hmap = defaultdict(int)
        for n in arr:
            hmap[n] += 1
        res = -1
        for k, v in hmap.items():
            if k == v:
                res = max(res, k)
        return res