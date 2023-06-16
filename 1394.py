from collections import defaultdict
def findLuckyInteger(arr):
    frequencyCount = defaultdict(int)
    ans = -1
    for x in arr:
        frequencyCount[x] +=1
    for y in frequencyCount:
        if frequencyCount[y] == y:
            ans = max(ans,y)
    return ans




print(findLuckyInteger( [2,2,3,4]))