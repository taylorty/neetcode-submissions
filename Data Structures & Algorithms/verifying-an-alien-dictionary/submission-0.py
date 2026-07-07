class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {}
        for index, char in enumerate(order):
            m[char] = index
        i = 0
        j = 1
        while j < len(words):
            word1 = words[i]
            word2 = words[j]
            for k in range(min(len(word1), len(word2)) + 1):
                if k == min(len(word1), len(word2)) and len(word1) > len(word2):
                    return False
                elif k == min(len(word1), len(word2)):
                    break
                if word1[k] != word2[k]:
                    if m[word1[k]] > m[word2[k]]:
                        return False
                    else:
                        break
                
            i += 1 
            j += 1
        return True
            