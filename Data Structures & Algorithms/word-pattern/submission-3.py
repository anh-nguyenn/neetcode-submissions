class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        hmap = defaultdict(str)
        j = 0
        for ch in pattern:
            tmp = ""
            while j < len(s) and s[j] != " ":
                tmp += s[j]
                j += 1
            if hmap[ch] == "" and tmp not in hmap.values():
                hmap[ch] = tmp
            if hmap[ch] != tmp:
                return False
            j += 1
        return True