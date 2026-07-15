import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        m_stones = [-x for x in stones]
        heapq.heapify(m_stones)
        while len(m_stones) > 1:
            x = - heapq.heappop(m_stones)
            y = - heapq.heappop(m_stones)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(m_stones, x - y)
            else:
                heapq.heappush(m_stones, y - x)
        return 0 if len(m_stones) == 0 else - m_stones[0]
        