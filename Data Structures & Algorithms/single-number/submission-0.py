class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        for key, val in mp.items():
            if val == 1:
                return key

        