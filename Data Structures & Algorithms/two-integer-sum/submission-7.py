class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build hashmap
        hmap = {}
        for idx, val in enumerate(nums):
            hmap[val] = idx
        for idx, val in enumerate(nums):
            remain = target - val
            if remain in hmap and idx != hmap[remain]:
                return sorted([idx, hmap[remain]])
            