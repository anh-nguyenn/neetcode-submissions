# Format: <length>%<string>
# dummy_input=["HelloHello","World"]
# en = 10%HelloHello5%World
class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_val = ""
        for word in strs:
            encode_val += str(len(word)) + "%" + word
        print(encode_val)
        return encode_val

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            print(i)
            while s[j] != "%":
                j += 1
            print(j)
            tmp_len = int(s[i:j])
            print('temp len: ', tmp_len)
            res.append(s[j+1:j+1+tmp_len])
            i = j+1+tmp_len
        return res
