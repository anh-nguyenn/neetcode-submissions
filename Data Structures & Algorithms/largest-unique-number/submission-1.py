class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        unique = set()
        seen = set()
        for n in nums:
            if n in unique:
                # seen.add(n)
                unique.remove(n)
            else:
                unique.add(n)
        if unique:
            return max(unique)
        else:
            return  -1