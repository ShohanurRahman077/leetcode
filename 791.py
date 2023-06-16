from collections import defaultdict
def customSortString(order: str, s: str) -> str:
        orderPos = {}
        sFrequency = {}
        freqCount = defaultdict(int)
        for x in range(len(order)):
            orderPos[order[x]] = x
        res = []
        ans =[]
        for y in s:
            freqCount[y]+=1
            if y in orderPos:
                sFrequency[orderPos[y]] = y
            else:
                res.append(y)
        for i in range(len(sFrequency)):
            for j in range(freqCount[sFrequency[i]]):
                ans.append(sFrequency[i])
        for j in res:
            ans.append(j)
        return "".join(ans)
customSortString(order="disqyr", s="iwyrysqrdj")