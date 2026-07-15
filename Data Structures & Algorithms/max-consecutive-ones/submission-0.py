class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = cnt = 0
        for item in nums:
            if item == 0:
                cnt = 0
                continue
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt