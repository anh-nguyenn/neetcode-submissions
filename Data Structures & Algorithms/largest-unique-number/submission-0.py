class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] += 1
        res = -1
        for k, v in hmap.items():
            if v == 1:
                res = max(k, res)
        return res
        