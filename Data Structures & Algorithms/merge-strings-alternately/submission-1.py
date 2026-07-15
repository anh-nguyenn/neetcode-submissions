class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return word2 or word1
        res = ""
        i, j = 0,0
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i, j = i + 1, j + 1
        # while i < l1:
        #     res += word1[i]
        #     i += 1
        # while j < l2:
        #     res += word2[j]
        #     j += 1
        if i == len(word1):
            res += word2[j:]
        else:
            res += word1[i:]
        return res
