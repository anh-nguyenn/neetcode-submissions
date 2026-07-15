import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_distance(x, y):
            return x*x + y*y
        d_map = defaultdict(list)
        distance = []
        for x, y in points:
            d = cal_distance(x, y)
            d_map[-d].append([x, y])
            distance.append(-d)
        heapq.heapify(distance)

        res = []
        while len(distance) > k:
            heapq.heappop(distance)
        while len(res) < k:
            dist = heapq.heappop(distance)
            for val in d_map[dist]:
                res.append(val)
        return res

        