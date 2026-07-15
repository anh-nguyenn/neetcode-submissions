class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        shortest_len = min([len(item) for item in strs])
        i = 0
        while i < shortest_len:
            ref = strs[0][i]
            for word in strs:
                if word[i] != ref:
                    return ''.join(res)
            res.append(ref)
            i += 1
        return ''.join(res)