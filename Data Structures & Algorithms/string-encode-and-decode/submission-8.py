class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            le = len(word)
            encode +=  str(le) + "+" + word 
        print(encode)
        return encode
    def decode(self, s: str) -> List[str]:
        decode = []
        i = j = 0
        while i < len(s):
            while s[j] != "+":
                j += 1
            # print(i, j)
            tmp_len = int(s[i:j])
            print(tmp_len)
            decode.append(s[j+1:j+1+tmp_len])
            i = j + tmp_len + 1
            j = i
        
        return decode

