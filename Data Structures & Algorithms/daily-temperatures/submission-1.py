class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp, idx
        # monotonic decreasing stack
        for idx, item in enumerate(temperatures):
            while stack and stack[-1][0] < item:
                IT, ID = stack.pop()
                res[ID] = idx - ID
            stack.append([item, idx])
        return res

        