class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(s) == 1:
            return s
        for item in shift:
            dr = item[0]
            am = item[1]
            tmp = ""
            if dr == 0:
                tmp = s[am:] + s[:am]

            else:
                shift = len(s) - am
                tmp = s[shift:] + s[:shift]
            print(tmp)
            s = tmp
        return s
            
            
