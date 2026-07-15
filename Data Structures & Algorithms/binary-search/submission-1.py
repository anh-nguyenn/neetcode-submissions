class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(nums[mid])
            if target < nums[mid]: # target on the left side
                right = mid - 1
            elif target > nums[mid]: # target on right
                left = mid + 1
            else:
                return mid
        print(left, right)
        return -1
            

        