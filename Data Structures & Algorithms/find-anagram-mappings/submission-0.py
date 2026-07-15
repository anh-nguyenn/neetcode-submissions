class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # First solution: O(n^2)
        mapping = []
        for val in nums1:
            for idx2, val2 in enumerate(nums2):
                if val2 == val:
                    mapping.append(idx2)
                    break
        return mapping