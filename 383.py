from collections import defaultdict,Counter

def canConstruct(ransomNote, magazine):
    ransomNoteDict = defaultdict(int)
    magazineDict = defaultdict(int)
    for x in ransomNote:
        ransomNoteDict[x] +=1
    for y in magazine:
        magazineDict[y] +=1
    res =0
    for i in ransomNoteDict:
        if magazineDict[i] >= ransomNoteDict[i]:
            res = res + ransomNoteDict[i]
    return len(list(ransomNote)) == res

print(canConstruct("aa", "aab"))