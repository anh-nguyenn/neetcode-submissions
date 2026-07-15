class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            mid = (e+s)//2
            
            mergeSort(arr, s, mid)
            mergeSort(arr, mid + 1, e)
            
            merge(arr, s, mid, e)

            return arr

        def merge(arr, s, mid, e):
            arr1 = arr[s:mid+1]
            arr2 = arr[mid+1:e+1]
            res = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            while i < len(arr1):
                res.append(arr1[i])
                i += 1
            while j < len(arr2):
                res.append(arr2[j])
                j += 1
            arr[s:e+1] = res
        return mergeSort(nums, 0, len(nums) - 1)