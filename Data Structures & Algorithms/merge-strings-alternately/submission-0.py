class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return word2 or word1
        res = ""
        l1, l2 = len(word1), len(word2)
        i, j = 0,0
        while i < l1 and j < l2:
            res += word1[i] + word2[j]
            i, j = i + 1, j + 1
        while i < l1:
            res += word1[i]
            i += 1
        while j < l2:
            res += word2[j]
            j += 1
        return res
