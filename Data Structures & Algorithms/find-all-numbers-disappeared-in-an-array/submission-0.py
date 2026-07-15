class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check = [0] * (len(nums) + 1)
        res = []
        for n in nums:
            check[n] += 1
        for j in range(1, len(check)):
            if check[j] == 0:
                res.append(j)
        
        return res