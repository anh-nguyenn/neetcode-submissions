class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        res = []
        for item in nums:
            if item == 0:
                cnt += 1
                continue
            res.append(item)
        for _ in range(cnt):
            res.append(0)
        nums[:] = res
        return nums
        