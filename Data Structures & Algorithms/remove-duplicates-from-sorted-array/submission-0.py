class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        res = []
        for n in nums:
            if n not in seen:
                res.append(n)
            seen.add(n)
        nums[:] = res
        return len(nums)