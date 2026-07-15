# Sorting with 2 pointers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()
        i , j = 0, len(A) - 1
        while i < j:
            temp = A[i][0] + A[j][0]
            if temp > target:
                j -= 1
            if temp < target:
                i += 1
            if temp == target:
                return [min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
        return []
        