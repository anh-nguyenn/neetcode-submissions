class Solution:
    def maxDifference(self, s: str) -> int:
        hmap = {}
        for ch in s:
            hmap[ch] = hmap.get(ch, 0) + 1
        # max_odd, min_even
        max_odd = float('-inf')
        min_even = float('inf')
        for val in hmap.values():
            if val % 2 == 1 and val > max_odd:
                max_odd = val
            if val % 2 == 0 and val < min_even:
                min_even = val
        return max_odd - min_even
        