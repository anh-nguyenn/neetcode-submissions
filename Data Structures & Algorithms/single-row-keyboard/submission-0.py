class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        '''
        cnt = 2
        cnt = 1
        '''
        res = []
        for ch in word:
            cnt = 0
            for k in keyboard:
                if k == ch:
                    break
                cnt += 1
            res.append(cnt)
        total = res[0]
        for i in range(1, len(res)):
            total += abs(res[i] - res[i-1])
        return total