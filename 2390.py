def removeStars(s):
    ans = []

    for x in s:
        if ans and x == '*':
            ans.pop()
        else:
            ans.append(x)
    return "".join(ans)
print(removeStars("leet**cod*e"))