class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        left, right = 0, len(heights) - 1
        while left < right:
            tmp = (min(heights[right], heights[left]))*(right - left)
            max_area = max(max_area, tmp)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return max_area

