import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            smallest = self.find_smallest(nums)
            for i in range(len(nums)):
                if nums[i] == smallest:
                    nums[i] = smallest * multiplier
                    break
        return nums
    
    def find_smallest(self, arr):
        smallest = float('inf')
        for item in arr:
            if item < smallest:
                smallest = item
        return smallest
