class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p1 = 1
        for n in nums:
            p1 *= n
        p2 = 1
        cnt = 0
        for n in nums:
            if n == 0:
                cnt += 1
                continue
            p2 *= n
        
        if cnt > 1:
            return [0]*len(nums)
        res = []
        if cnt == 1:
            for n in nums:
                if n == 0:
                    res.append(p2)
                    continue
                res.append(0)
        else:
            for n in nums:
                res.append(p1//n)
        return res

        