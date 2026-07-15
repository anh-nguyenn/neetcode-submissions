class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bi_posi = (n >> i)&1 # Go to right most position, & 1
            val = bi_posi << (31 - i) # Go to left most position
            res += val
        return res


'''
n = 00010110
reverse → 01101000
'''
        