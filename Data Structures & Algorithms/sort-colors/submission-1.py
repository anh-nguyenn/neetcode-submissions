class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f = [0]*3
        for num in nums:
            f[num] += 1
        # [1, 2, 1]
        s = 0
        for i in range(3):
            while f[i]:
                nums[s] = i
                f[i] -= 1
                s += 1
        