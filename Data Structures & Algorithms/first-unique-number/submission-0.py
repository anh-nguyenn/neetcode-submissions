class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hmap = defaultdict(int)
        for n in nums:
            self.hmap[n] += 1

    def showFirstUnique(self) -> int:
        for k, v in self.hmap.items():
            if v == 1:
                return k
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.hmap[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
