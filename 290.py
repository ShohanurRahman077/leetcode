from collections import defaultdict
def wordPattern(pattern: str, s: str) -> bool:
        patternFreq = defaultdict(int)
        sFrequency = defaultdict(int)
        for x in pattern:
            patternFreq[x] +=1
        for y in s.split():
            sFrequency[y]+=1
        print(patternFreq, sFrequency)
        return sorted(patternFreq.values()) == sorted(sFrequency.values())



print(wordPattern(pattern = "aba", s = "dog cat cat"))