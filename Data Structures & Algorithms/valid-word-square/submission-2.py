class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        max_len = max(len(w) for w in words)
        for i in range(n):
            while len(words[i]) < max_len:
                words[i] += "#"
        print(words)
        for i in range(n):
            item = words[i]
            comp = ""
            for j in range(n):
                comp += words[j][i]
            print(item, comp)
            if item != comp:
                return False
        return True