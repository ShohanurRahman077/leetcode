def validParenthesis(str):
    stack = []
    matching = {"(": ")", "[": "]", "{": "}"}

    for c in str:
        if c in matching:  # if c is an opening bracket
            stack.append(c)
        else:
            if not stack:
                return False

            previous_opening = stack.pop()
            if matching[previous_opening] != c:
                return False

    return not stack


s = "()[]{}"
validParenthesis(s)
