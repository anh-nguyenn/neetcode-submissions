class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [3,4,5,6,1,2]
        
        [6,1,2,3,4,5]

        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]: # left half is sorted
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else: 
                    right = mid
            else: # right half is sorted
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid 
        return -1



        