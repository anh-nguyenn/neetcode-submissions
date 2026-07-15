class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbr
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i, j = i + 1, j + 1
            else:
                if abbr[j] == "0":
                    return False
                cnt = 0
                while j < len(abbr) and abbr[j].isnumeric():
                    cnt = 10 * cnt + int(abbr[j])
                    j += 1
                i += cnt
        return i == len(word) and j == len(abbr)