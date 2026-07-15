# Format: 5#Hello5#World
# i = 0, j = 1
class Solution:

    def encode(self, strs: List[str]) -> str:
        self.enStr = ""
        for word in strs:
            self.enStr += str(len(word))+"#" + word
        # print(self.enStr)
        return self.enStr

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        # i keep track idx
        # j keep track #
        while i < len(s):
            while s[j] != "#":          
                j += 1
            tmpLen = int(s[i:j])
            print(s[i:j])
            res.append(s[j+1:j+1+tmpLen]) 
            # print(s[j+1:j+1+tmpLen])
            i = j+1+tmpLen
            j = i
        return res

