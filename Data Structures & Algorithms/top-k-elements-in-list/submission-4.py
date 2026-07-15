class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build hmap
        hmap = defaultdict(int)
        for val in nums:
            hmap[val] += 1

        res = set()
        freq = sorted(hmap.values(), reverse = True)
        print(freq)
        for i in range(k):
            #freq[i]
            for k, v in hmap.items():
                if v == freq[i]:
                    res.add(k)
        print(res)
        return list(res)
