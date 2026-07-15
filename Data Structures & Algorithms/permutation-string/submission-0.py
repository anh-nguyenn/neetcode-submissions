class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = ''.join(sorted(s1))
        print(S1)
        L = 0
        R = len(s1) - 1
        while R < len(s2):
            if S1 == ''.join(sorted(s2[L:R+1])):
                return True
            print(s2[L:R+1])
            L += 1
            R += 1
        return False