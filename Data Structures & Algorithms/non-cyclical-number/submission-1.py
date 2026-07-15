class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        

        while True:
            total = 0
            while n > 0:
                total += (n % 10)**2
                n /= 10
                n = int(n)
                total = int(total)
            n = total
            if n in visit:
                return False
            if total == 1:
                return True
            visit.add(n)


            
            