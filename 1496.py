def isPathCrossing(path):
    x,y =0,0
    pathSet = set()
    pathSet.add("0_0")
    for i in path:
        if i == "N": y+=1
        elif i == "E": x+=1
        elif i == "S": y-=1
        else: x-=1
        key = f"{x}_{y}"
        if key in pathSet:
            return True
        pathSet.add( f"{x}_{y}")
    return False
print(isPathCrossing("NES"))