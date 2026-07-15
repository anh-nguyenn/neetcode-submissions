class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre and pos fix

        def prefixP(nums):
            pre = [nums[0]]
            for i in range(1, len(nums)):
                pre.append(pre[-1]*nums[i])
            return pre
        def posfixP(nums):
            pos = [nums[-1]]
            for i in range(len(nums) - 2, -1, -1):
                pos.append(pos[-1]*nums[i])
            return pos[::-1]
        res = []
        pre = prefixP(nums)
        pos = posfixP(nums)
        for i in range(len(nums)):
            if i == 0:
                res.append(pos[1])
            elif i == len(nums) - 1:
                res.append(pre[-2])
            else: 
                res.append(pre[i-1]*pos[i+1])
        return res