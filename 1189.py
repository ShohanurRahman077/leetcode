from collections import defaultdict
def maxNumberOfBalloons(text):
    counts = {'b':0,'a':0,'l':0,'o':0,'n':0}
    for x in text:
        if x in counts:
            counts[x] +=1
    return (min(counts['b'],counts['a'],counts['l']/2,counts['o']/2,counts['n']) )
print(maxNumberOfBalloons("leetcode"))

