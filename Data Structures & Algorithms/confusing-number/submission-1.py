class Solution:
    def confusingNumber(self, n: int) -> bool:
        INVALID = {2,3,4,5,7}
        MAP = {0:0 , 1: 1, 6:9, 8: 8, 9: 6}
        res = ""
        m = n
        if n == 0: return False

        while n > 0:
            num = n % 10
            if num in INVALID:
                return False
            val = MAP[num]
            res += str(val)
            n //= 10
        return True if int(res) != m else False
