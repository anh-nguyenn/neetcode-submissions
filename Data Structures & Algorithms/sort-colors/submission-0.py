class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quickSort(arr, s, e):
            if (e-s+1 <= 1):
                return arr
            pivot = arr[e]
            left = s
            for i in range(s, e+1):
                if arr[i] < pivot:
                    arr[i], arr[left] = arr[left], arr[i]
                    left += 1
                
            arr[e] = arr[left]
            arr[left] = pivot
            quickSort(arr, s, left - 1)
            quickSort(arr, left + 1, e)
            return arr
        
        return quickSort(nums, 0, len(nums) - 1)
        