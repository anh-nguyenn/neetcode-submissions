class Solution:
    def minOperations(self, logs: List[str]) -> int:
        '''
        d1/d2/
        d1/d21
        '''
        res = []
        for item in logs:
            if "../" in item:
                if len(res) == 0:
                    continue
                res.pop()
            elif "./" in item:
                continue
            else:
                res.append(1)
        return len(res)