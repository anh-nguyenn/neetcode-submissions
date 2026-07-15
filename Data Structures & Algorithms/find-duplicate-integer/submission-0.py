class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        for n in nums:
            mp[n] = 1 + mp.get(n, 0)
        maxK = 100001
        mp[maxK] = 0

        for k, v in mp.items():
            if v > mp[maxK]:
                maxK = k
        return maxK