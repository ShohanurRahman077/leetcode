from collections import defaultdict
def frequencySort(s):
    ans=""
    frequencyCount = defaultdict(int)
    for x in s:
        frequencyCount[x]+=1
    frequencyCount = dict(sorted(frequencyCount.items(), key=lambda item: item[1], reverse =True))
    for i in frequencyCount:
        for j in range(frequencyCount[i]):
            ans+=i

    return ans


print(frequencySort("cccaaa"))