class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for n in digits:
            res += str(n)
        ans = []
        for ch in str(int(res) + 1):
            ans.append(ch)
        return ans
        