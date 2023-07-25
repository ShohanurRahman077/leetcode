def simplifyPath(str):
    listOfElement = str.split("/")
    inputStack = []
    for x in listOfElement:
        if x == "..":
            if inputStack:
                inputStack.pop(x)
        elif x == "." or not x:
            continue
        else:
            inputStack.append(x)
    

    return "/" + "/".join(inputStack)





print(simplifyPath("/home/"))