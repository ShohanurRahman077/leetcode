from collections import defaultdict
def closeStrings(word1: str, word2: str) -> bool:
        word1Freq = defaultdict(int)
        word2Freq = defaultdict(int)

        if len(word1) != len(word2):
            return False
        
        for x in range(len(word1)):
            word1Freq[word1[x]]+=1
            word2Freq[word2[x]]+=1
        return (sorted(word1Freq.values()) == sorted(word2Freq.values())) and (sorted(word1Freq.keys()) ==sorted(word2Freq.keys()))



closeStrings(word1="uau",word2="ssx")