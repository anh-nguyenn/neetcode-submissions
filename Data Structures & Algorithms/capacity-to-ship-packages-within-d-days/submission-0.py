class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right
        while left <= right:
            m = (left + right)//2
            tmp = 0
            counter = 1
            for w in weights:
                # max cap is m
                if tmp + w > m:
                    tmp = 0
                    counter += 1
                tmp += w
            if counter <= days:
                res = m
                right = m - 1
            else:
                left = m + 1
        return res

