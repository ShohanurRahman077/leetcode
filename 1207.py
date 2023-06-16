from collections import defaultdict
def uniqueNumberOfOccurrence(arr):
    frequencyCount = defaultdict(int)
    ans = set()
    for x in arr:
        frequencyCount[x] +=1
    print(frequencyCount)
    for y in frequencyCount:
        if frequencyCount[y] in ans:
            return False
        ans.add(frequencyCount[y])

    return True




print(uniqueNumberOfOccurrence([-3,0,1,-3,1,1,1,-3,10,0]))