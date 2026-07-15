class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        res = []
        for item in nums:
            if item != val:    
                res.append(item)
        nums[:] = res
        return len(nums)
        