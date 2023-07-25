class Solution:
    def removeDuplicates(self, s: str) -> str:
        inputStack = []
        res = ""
        for x in s:
            if inputStack:
                top_element = inputStack[-1]
                if top_element == x:
                    inputStack.pop()
                else:
                    inputStack.append(x)
            else: 

                inputStack.append(x)
        return (res.join(inputStack))