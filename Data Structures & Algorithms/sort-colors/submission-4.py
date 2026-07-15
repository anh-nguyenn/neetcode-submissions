class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # freq array
        freq = [0]*3

        for n in nums: # freq array
            freq[n] += 1
        idx = 0
        for i in range(3): # i = 0, 1, 2
            while freq[i]: # for freqency of val at idx
                nums[idx] = i
                idx += 1
                freq[i] -= 1