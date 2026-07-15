import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[:]

        min_heap = [(val, idx) for idx, val in enumerate(nums)]
        
        heapq.heapify(min_heap)
        print(min_heap)
        for _ in range(k):
            smallest, index = heapq.heappop(min_heap)     
            adder = smallest * multiplier
            heapq.heappush(min_heap, (adder, index))
            res[index] = adder
        return res