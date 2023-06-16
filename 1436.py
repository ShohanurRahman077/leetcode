from collections import defaultdict
def destinationCity(paths: list[list[str]]):
    dict = defaultdict(list)
    for x in paths:
        dict[x[0]].append(x[1])
            
    for x in paths:
        for y in x:
            if y not in dict:
                return y

def destinationCity2(paths: list[list[str]]):
    dict = defaultdict(list)
    ans = ''        
    for x in paths:
        for y in x:
            ans = y
    
    return ans



print(destinationCity2([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))