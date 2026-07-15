class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for n in nums:
            tmp = self.prefix[-1]
            self.prefix.append(tmp + n)
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)