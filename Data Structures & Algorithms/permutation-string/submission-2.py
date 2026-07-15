class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        setS1 = set(s1)
        sortedS1 = ''.join(sorted(s1))
        k = len(s1)
        for i in range(len(s2)):
            # print(s2[i])
            if s2[i] in setS1:
                if ''.join(sorted(s2[i:i+k])) == sortedS1:
                    return True
        return False