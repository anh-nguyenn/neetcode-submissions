import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        print(max_heap)
        for _ in range(k):
            biggest = heapq.heappop(max_heap)
            sq = int(-math.sqrt(-biggest))
            heapq.heappush(max_heap, sq)
        return - sum(max_heap)
        