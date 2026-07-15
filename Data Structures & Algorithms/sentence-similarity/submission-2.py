class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        for i in range(len(sentence1)):
            s1 = sentence1[i]
            s2 = sentence2[i]
            if s1 == s2:
                continue
            found = False
            for j in range(len(similarPairs)):
                if s1 in similarPairs[j] and s2 in similarPairs[j]:
                    found = True
                    break
            if not found:
                return False
        return True
            