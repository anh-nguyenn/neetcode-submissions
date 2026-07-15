class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for item in operations:
            if item == "+":
                res.append(res[-1] + res[-2])
            elif item == "D":
                res.append(2*res[-1])
            elif item == "C":
                res.pop()
            else:
                res.append(int(item))
        return sum(res)