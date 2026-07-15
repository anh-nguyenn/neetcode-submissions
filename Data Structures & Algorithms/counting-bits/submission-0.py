class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for k in range(n+1):
            cnt = 0
            while k > 0:
                if k & 1 == 1:
                    cnt += 1
                k = k // 2
            res.append(cnt)
        return res
