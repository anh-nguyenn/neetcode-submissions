class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        M = {}
        for num in nums:
            M[num] = 1 + M.get(num, 0)
        # how to sort val in dict

        top_k = tuple(sorted(M.values(), reverse = True)[:k])
        res = []
        for k,v in M.items():
            if v in top_k:
                res.append(k)
        return res


