from collections import defaultdict
def numJewelsInStones(jewels, stones):
    stonesCount = defaultdict(int)
    for x in stones:
        stonesCount[x] +=1
    numJewelsInStones = 0
    for y in jewels:
        numJewelsInStones += stonesCount[y]
    return numJewelsInStones





numJewelsInStones("aA",  "aAAbbbb")