class Solution:
    def countElements(self, arr: List[int]) -> int:
        bucket = [0]*1001
        for item in arr:
            bucket[item] += 1
        res = 0
        for i in range(1, 1001):
            if bucket[i] != 0 and bucket[i-1] != 0:
                res += bucket[i-1]
        return res

        