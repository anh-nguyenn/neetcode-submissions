class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build hashmap
        hmap = {}
        for idx, val in enumerate(nums):
            remain = target - val
            if remain in hmap:
                return [hmap[remain], idx]
            hmap[val] = idx
        return []
            