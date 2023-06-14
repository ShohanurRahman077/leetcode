from collections import defaultdict
def zeroOneLoose(matches):
    winnerList = defaultdict(int)
    looserList = defaultdict(int)
    winnerResult = []
    looserResult = []
    for x in matches:
        winnerList[x[0]] +=1
        looserList[x[1]] +=1
    for y in winnerList:
        if y not in looserList:
            winnerResult.append(y)
    for z in looserList:
        if looserList[z] == 1:
            looserResult.append(z)
    return [sorted(winnerResult),sorted(looserResult)]


    




print(zeroOneLoose([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))