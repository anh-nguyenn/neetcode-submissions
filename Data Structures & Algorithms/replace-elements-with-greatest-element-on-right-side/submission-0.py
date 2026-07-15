class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)
        if n == 1:
            return [-1]     
        for i in range(n - 1):
            arr[i] = max(arr[i+1:])
        arr[n-1] = -1
        return arr
        

        