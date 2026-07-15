class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        res = []
        n = len(temperatures)
        for i in range(n):
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
                if j == n - 1:
                    res.append(0)
        return res
        