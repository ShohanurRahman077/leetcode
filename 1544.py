def makeGood(s: str) -> str:
    inputStack = []
    for x in s:
        if inputStack:
            top = inputStack[-1]
            if (top.upper() == x.upper()) and ((top.islower() and x.isupper()) or ((top.isupper() and x.islower()))):
                inputStack.pop()
            else:
                inputStack.append(x)
        else:    
            inputStack.append(x)
    return "".join(inputStack)

print(makeGood("abBAcC"))