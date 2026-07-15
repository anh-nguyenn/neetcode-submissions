class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [2,2,3,4,5] => pre*pos
        # pre = [1, 2, 4 , 12, 48]      
        pre = 1
        res = []
        for num in nums:
            res.append(pre)
            pre *= num
        pos = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= pos
            pos *= nums[i]
        return res



    