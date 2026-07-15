class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        res = []
        for i, num in enumerate(nums):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            res.append(product)
        return res