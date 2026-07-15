class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hmap1 = {}
        hmap2 = {}
        res = []
        for idx, val in enumerate(nums2):
            hmap2[val] = idx
        for num in nums1:
            res.append(hmap2[num])
        return res