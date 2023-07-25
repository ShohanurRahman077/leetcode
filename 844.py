class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for x in s:
            if s_stack and x =="#":
                s_stack.pop()
            else:
                if x != "#":
                    s_stack.append(x)
        for x in t:
            if t_stack and x =="#":
                t_stack.pop()
            else:
                if x != "#":
                    t_stack.append(x) 
        print(s_stack)
        print(t_stack)
        return "".join(s_stack) == "".join(t_stack)