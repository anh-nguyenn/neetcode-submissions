class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # using sliding window of fixed size
        window = set() # set of cur window of size <= k
        L = 0 # to be increment when window change 

        for R in range(len(nums)):
            # edit size of window before checking
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
