# b keeps track of the lowest buy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        maxProfit = 0
        while s < len(prices):
            if prices[s] > prices[b]:
                maxProfit = max(maxProfit, prices[s] - prices[b])
            else:
                # the day has a lower price, update b
                b = s
            # go to next day
            s += 1
        return maxProfit
