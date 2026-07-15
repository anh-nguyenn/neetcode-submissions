# Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, arr, s, e):
        if e-s+1 <= 1:
            return arr
        m = (e+s)//2
        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m+1, e)
        
        self.merge(arr, s, m, e)
        
        return arr

    def merge(self, arr, s, m, e):
        # Copy 
        L = arr[s:m+1]
        R = arr[m+1:e+1]
        
        i, j, k = 0, 0, s
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        if i < len(L):
            arr[k:e+1] = L[i:]
        else:
            arr[k:e+1] = R[j:]

    