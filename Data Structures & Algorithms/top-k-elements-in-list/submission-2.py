class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to store idx => [] value with this frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # get hashmap
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # fill freq map
        for n in nums:
            getCount = count[n]
            freq[getCount].append(n)
        print(freq)
        res = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                print("B")
                if num not in res:
                    print("A")
                    res.append(num)
                if len(res) == k:
                    return res
            
            

                


        

        
